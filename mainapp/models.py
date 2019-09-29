from django.db import models


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


class Picture(Core):
    """ Класс изображений - родитель для других моделей использующих изображения """
    class Meta:
        ordering = ('sort', 'updated')
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    image = models.ImageField(upload_to='images')
    related_obj = models.ForeignKey(Core, verbose_name='изображения', null=True, blank=True, related_name='images', on_delete=models.CASCADE)


class Category(Core):
    """Класс описывающий вид животного"""


class PetGender(Core):
    """Класс описывающий пол животного"""


class PetSize(Core):
    """Класс описывающий размеры животного"""


class PetWool(Core):
    """Класс описывающий длину шерсти животного"""


class PetColor(Core):
    """Класс описывающий цвет животного"""


class PetCharacter(Core):
    """Класс описывающий характер животнго"""


# добавить особенности (теги), например нет глаза и т.д.


class Pet(Core):
    """Класс описывающий животного"""
    pet_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pet_gender = models.ForeignKey(PetGender, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(verbose_name='возраст (лет)', default=0)
    month = models.PositiveIntegerField(verbose_name='возраст (мес)', default=0)
    pet_size = models.ForeignKey(PetSize, on_delete=models.CASCADE)
    pet_wool_length = models.ForeignKey(PetWool, on_delete=models.CASCADE)
    pet_color = models.ForeignKey(PetColor, on_delete=models.CASCADE)
    pet_character = models.ForeignKey(PetCharacter, on_delete=models.CASCADE)

    # Убираем из каталога неактивные объявления
    @staticmethod
    def get_items():
        return Pet.objects.filter(is_active=True, category__is_active=True).order_by('category', 'name')
