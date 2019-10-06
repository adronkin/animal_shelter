from .models import Menu


def get_context(request):
    """
    Контекст для шаблонов в виде пар 'ключ' - 'значение':
    'menu' - главное меню, меню приютов и питомцев..., url-ссылки, css-классы...
    """
    context = {
        'menu': Menu(),
    }
    return context
