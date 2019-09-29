from django.db import models


class Category(models.Model):
	"""Класс описывающий вид животного"""
	name = models.CharField(verbose_name='вид', max_length=64, unique=True)  # кошка или собака
	description = models.TextField(verbose_name='описание', blank=True)  # нужно ли?
	is_active = models.BooleanField(verbose_name='активность', default=True)

	def __str__(self):
		return self.name


class PetGender(models.Model):
	"""Класс описывающий пол животного"""
	gender = models.CharField(verbose_name='пол', max_length=16, unique=True)
	is_active = models.BooleanField(verbose_name='активность', default=True)

	def __str__(self):
		return self.gender


class PetSize(models.Model):
	"""Класс описывающий размеры животного"""
	size = models.CharField(verbose_name='размер', max_length=16, unique=True)
	is_active = models.BooleanField(verbose_name='активность', default=True)

	def __str__(self):
		return self.size


class PetWool(models.Model):
	"""Класс описывающий длину шерсти животного"""
	wool_length = models.CharField(verbose_name='длина шерсти', max_length=16, unique=True)
	is_active = models.BooleanField(verbose_name='активность', default=True)

	def __str__(self):
		return self.wool_length


class PetColor(models.Model):
	"""Класс описывающий цвет животного"""
	color = models.CharField(verbose_name='цвет', max_length=32, unique=True)
	is_active = models.BooleanField(verbose_name='активность', default=True)

	def __str__(self):
		return self.color


class PetCharacter(models.Model):
	"""Класс описывающий характер животнго"""
	character = models.CharField(verbose_name='характер', max_length=32, unique=True)
	is_active = models.BooleanField(verbose_name='активность', default=True)

	def __str__(self):
		return self.character


# добавить особенности (теги), например нет глаза и т.д.


class Pet(models.Model):
	"""Класс описывающий животного"""
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	pet_name = models.CharField(verbose_name='имя', max_length=64)
	pet_gender = models.ForeignKey(PetGender, on_delete=models.CASCADE)
	age = models.PositiveIntegerField(verbose_name='возраст (лет)', default=0)
	month = models.PositiveIntegerField(verbose_name='возраст (мес)', default=0)
	pet_size = models.ForeignKey(PetSize, on_delete=models.CASCADE)
	pet_wool_length = models.ForeignKey(PetWool, on_delete=models.CASCADE)
	pet_color = models.ForeignKey(PetColor, on_delete=models.CASCADE)
	pet_character = models.ForeignKey(PetCharacter, on_delete=models.CASCADE)
	description = models.TextField(verbose_name='описание', blank=True)
	image = models.ImageField(upload_to='pet_photo', blank=True)
	is_active = models.BooleanField(verbose_name='активность', default=True)

	def __str__(self):
		return self.pet_name

	# Убираем из каталога неактивные объявления
	@staticmethod
	def get_items():
		return Pet.objects.filter(is_active=True, category__is_active=True).order_by('category', 'name')
