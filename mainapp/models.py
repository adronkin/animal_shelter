from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.conf import settings


class Core(models.Model):
    """ Класс ядро - родитель всех классов-моделей """

    class Meta:
        ordering = ('-is_active', 'sort', 'name')
        verbose_name = 'Ядро'
        verbose_name_plural = 'Ядра'

    name = models.CharField(verbose_name='заголовок объекта', max_length=255, null=True)
    description = models.TextField(verbose_name='описание объекта', blank=True, null=True)
    sort = models.IntegerField(verbose_name='номер объекта для сортировки', default=0, blank=True, null=False)
    is_active = models.BooleanField(verbose_name='активен ли объект', default=True, db_index=True)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    def __str__(self):
        return f'{self.name}' if self.name else ''

    def delete(self, **kwargs):  # или может *args
        if 'force' in kwargs:
            super().delete()
        else:
            self.is_active = False
            self.save()


class Picture(Core):
    """ Класс изображений - родитель для других моделей использующих изображения """

    class Meta:
        ordering = ('sort', 'updated')
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    image = models.ImageField(upload_to='images')
    related_obj = models.ForeignKey(Core,
                                    verbose_name='изображения',
                                    null=True, blank=True,
                                    related_name='images',
                                    on_delete=models.CASCADE)


class City(Core):
    """ Класс для выбора города приюта / пользователя """


class Shelter(Core):
    """ Класс-модель приюта/питомника """
    shelter_logo = models.ImageField(upload_to='shelter/images', verbose_name='логотип приюта', blank=True)
    shelter_city = models.ForeignKey(City, verbose_name='город', related_name='shelters',
                                     null=False, blank=False, on_delete=models.PROTECT)
    shelter_address = models.CharField(verbose_name='адрес', max_length=255, null=False, blank=False, unique=True)
    shelter_phone = models.CharField(verbose_name='телефон', max_length=17, null=False, blank=False, unique=True)
    shelter_email = models.EmailField(verbose_name='эл.почта', null=False, blank=False, unique=True)
    shelter_cord_latitude = models.IntegerField(verbose_name='координаты - широта', default=0)
    shelter_cord_longitude = models.IntegerField(verbose_name='координаты - долгота', default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Donate(Core):
    """ Класс для финансовой помощи - Сбер, ЯндексДеньги, PayPal... """
    account = models.ForeignKey(Shelter,
                                verbose_name='реквизиты счетов',
                                blank=True,
                                related_name='accounts',
                                on_delete=models.PROTECT)


class Social(Core):
    """ Класс ссылок на соц.сети и мессенджеры """
    link = models.URLField(verbose_name='ссылка на соц.сеть', null=True, blank=True, unique=True)
    obj = models.ForeignKey(Shelter, related_name='links', on_delete=models.PROTECT)


class PetCategory(Core):
    """Класс описывающий вид животного"""


class PetStatus(Core):
    """ Класс описывающий состояние здоровья питомца и его готовность покинуть приют """


class PetBreed(Core):
    """Класс описывающий породу животного"""


class PetGender(Core):
    """Класс описывающий пол животного"""


class PetSize(Core):
    """Класс описывающий размеры животного"""


class PetWool(Core):
    """Класс описывающий длину шерсти животного"""


class PetColor(Core):
    """Класс описывающий цвет животного"""


class PetCharacter(Core):
    """Класс описывающий характер животного"""


class Pet(Core):
    """Класс описывающий животного"""
    pet_shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name='pets', blank=False, null=False)
    pet_category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    pet_status = models.ForeignKey(PetStatus, on_delete=models.CASCADE)
    pet_breed = models.ForeignKey(PetBreed, on_delete=models.CASCADE)
    pet_gender = models.ForeignKey(PetGender, on_delete=models.CASCADE)
    pet_size = models.ForeignKey(PetSize, on_delete=models.CASCADE)
    pet_wool_length = models.ForeignKey(PetWool, on_delete=models.CASCADE)
    pet_color = models.ForeignKey(PetColor, on_delete=models.CASCADE)
    pet_character = models.ForeignKey(PetCharacter, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(verbose_name='возраст (лет)', default=0)
    month = models.PositiveIntegerField(verbose_name='возраст (мес)', default=0)

    # Убираем из каталога неактивные объявления
    @staticmethod
    def get_items():
        return Pet.objects.filter(is_active=True).order_by('pet_category', 'name')

    @staticmethod
    def get_count(status=''):
        return Pet.objects.filter(is_active=True, pet_status__name__contains=status).count()


class MenuManager(models.Manager):
    """ Менеджер меню """

    def get_menu(self, attr):
        return self.filter(name=attr, parent_id__isnull=True).first()


class Menu(Core):
    """ Модель меню """

    class Meta:
        ordering = ('parent_id', 'sort', 'name')
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Меню сайта'

    url = models.CharField('ссылка', max_length=255, blank=False, null=False, default='#')
    css_class = models.CharField('CSS-Класс блока меню', max_length=30, null=False, blank=True, default='')
    seen_guests = models.BooleanField('виден незарегистрированным пользователям', default=True)
    seen_users = models.BooleanField('виден зарегистрированным пользователям', default=False)
    seen_shelters = models.BooleanField('виден приютам', default=False)
    parent = models.ForeignKey('self', verbose_name='суперкласс меню', null=True, blank=True, related_name='submenus',
                               on_delete=models.CASCADE)

    objects = MenuManager()

    def __getattr__(self, attr):
        if attr.startswith('get_menu_'):
            return type(self).objects.get_menu(attr[9:])
        return super().__getattr__(attr)

    def get_url(self):
        return reverse(self.url) if ':' in self.url else self.url


def create_menu_shelter(instance, created, **kwargs):
    """
    После добавления нового приюта, по сигналу, создает новый подпункт
    меню в пункте меню Приюты.
    """
    if created:
        Menu.objects.create(
            name=instance, sort=instance.id, url=f'/shelters/{instance.id}',
            seen_users=True, seen_shelters=True, parent=Menu.objects.get(name='Приюты')
        )


post_save.connect(create_menu_shelter, sender=Shelter)
