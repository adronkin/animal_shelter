from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from authapp.models import ActivateUser
from authapp.forms import RegisterForm


def register(response):
    if response.method == "POST":
        register_form = RegisterForm(response.POST)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                return redirect('login')
            else:
                print('ошибка отправки сообщения')
                return redirect('login')

    else:
        form = RegisterForm()
        return render(response, "registration/register.html", {"form": form})


def send_verify_mail(user):
    activate_user = get_object_or_404(ActivateUser, user_id=user.id)
    verify_link = reverse('verify', args=[user.email, activate_user.activation_key])

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

