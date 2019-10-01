from django.views.generic.base import TemplateView
from django.shortcuts import render


class Index(TemplateView):
    """ Главная страница """
    template_name = 'mainapp/index.html'


class Contact(TemplateView):
    """ Страница контактов интернет-магазина """
    template_name = 'mainapp/contact.html'


class About(TemplateView):
    """ Главная страница """
    template_name = 'mainapp/about.html'


class Cats(TemplateView):
    """Страница кошек"""
    template_name = 'mainapp/cats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'cats'
        context['href'] = 'main:cats'
        return context


class Dogs(TemplateView):
    """Страница кошек"""
    template_name = 'mainapp/dogs.html'


class Volunteer(TemplateView):
    """Страница добровольцев"""
    template_name = 'mainapp/volunteer.html'


class BlogHome(TemplateView):
    """Страница главная блога"""
    template_name = 'mainapp/blog-home.html'


class BlogSingle(TemplateView):
    """Страница single блога"""
    template_name = 'mainapp/blog-single.html'


class Elements(TemplateView):
    """Страница демострации"""
    template_name = 'mainapp/elements.html'

