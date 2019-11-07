from django.contrib import auth
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from authapp.models import ActivateUser
from authapp.forms import RegisterForm, ActivateEditForm, SystemEditForm, TypeOfUserEditForm
from reserveapp.models import Reserve


def register(response):
    if response.method == "POST":
        register_form = RegisterForm(response.POST)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                return HttpResponse('На Ваш почтовый ящик отправлено сообщение для активации аккаунта')
            else:
                print('ошибка отправки сообщения')
                return redirect('login')
        else:
            return HttpResponse('Форма заполнена неверно')
    else:
        form = RegisterForm()
        return render(response, "registration/register.html", {"form": form})


def send_verify_mail(user):
    activate_user = get_object_or_404(ActivateUser, user_id=user.id)
    verify_link = reverse('auth:verify', args=[user.email, activate_user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на портале ' \
              f'{settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        activate_user = get_object_or_404(ActivateUser, user_id=user.id)
        if activate_user.activation_key == activation_key and not activate_user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'registration/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'registration/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('main:index'))


@transaction.atomic
def edit(request):
    title = 'Edit profile'
    reserve_pets = Reserve.objects.filter(user=request.user)
    if request.method == 'POST':
        user_form = ActivateEditForm(request.POST, request.FILES, instance=request.user.activateuser)
        system_form = SystemEditForm(request.POST, instance=request.user)
        if system_form.is_valid() and user_form.is_valid():
            system_form.save()
            user_form.save()
            print()
            print("Функция view.edit (authapp) отработала сохранение системной и доп. информации пользователя...")
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        user_form = ActivateEditForm(instance=request.user.activateuser)
        system_form = SystemEditForm(instance=request.user)

    content = {'title': title, 'user_form': user_form, 'system_form': system_form}
    return render(request, 'edit.html', content)


@transaction.atomic
def edit_type_of_user(request):
    title = 'Edit profile'

    if request.method == 'POST':
        user_form = TypeOfUserEditForm(request.POST, request.FILES, instance=request.user.activateuser, auto_id=False)
        if user_form.is_valid():
            user_form.save()
            print()
            return HttpResponseRedirect(reverse('main:index'))

    else:
        user_form = TypeOfUserEditForm(instance=request.user.activateuser, auto_id=False)
    content = {'title': title, 'user_form': user_form}
    return render(request, 'type_of_user.html', content)
