from django.db import models
from django.urls import reverse
from django.conf import settings


class Work(models.Model):
    type_work = models.ForeignKey('TypeWork', on_delete=models.PROTECT, verbose_name='Эксп/Исл')
    number = models.CharField(max_length=150, verbose_name='Номер')
    serial_number = models.CharField(max_length=150, verbose_name='Номер дела')
    receipt_date = models.DateField(auto_now_add=False, verbose_name='Дата регистрации', blank=True)
    initiator = models.ForeignKey('Initiator', on_delete=models.PROTECT, verbose_name='Инициатор')
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name='Сотрудник', blank=True)
    subdivision = models.ForeignKey('Subdivision', on_delete=models.PROTECT, verbose_name='Подразделение', blank=False)
    completion_date = models.DateField(auto_now_add=False, verbose_name='Дата исполнения', blank=True, null=True)
    researched_objects = models.ManyToManyField('Researched_objects', verbose_name='Объекты', blank=True)
    additional_information = models.TextField(blank=True, verbose_name='Дополнительные сведения')
    renewal_date = models.DateField(auto_now_add=False, verbose_name='Дата продления', blank=True, null=True)


    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('view_work', kwargs={'work_id': self.pk})

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ['number']

class TypeWork(models.Model):
    type_work = models.CharField(max_length=150, verbose_name='Вид работы')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('type_work', kwargs={'type_work_id': self.pk})

    def __str__(self):
        return self.type_work

    class Meta:
        verbose_name = 'Тип материала'
        verbose_name_plural = 'Типы материалов'

class Initiator(models.Model):
    family_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    second_name = models.CharField(max_length=50, verbose_name='Отчество')
    rank = models.ForeignKey('Rank', on_delete=models.PROTECT, verbose_name='Звание')
    position = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')
    subdivision = models.ForeignKey('Subdivision', on_delete=models.PROTECT, verbose_name='Подразделение')

    def __str__(self):
        return self.family_name

    class Meta:
        verbose_name = 'Инициатор'
        verbose_name_plural = 'Инициаторы'

# class Employee(models.Model):
#     family_name = models.CharField(max_length=50, verbose_name='Фамилия')
#     first_name = models.CharField(max_length=50, verbose_name='Имя')
#     second_name = models.CharField(max_length=50, verbose_name='Отчество')
#     rank = models.ForeignKey('Rank', on_delete=models.PROTECT, verbose_name='Звание')

#    def __str__(self):
#        return self.family_name

#    class Meta:
#        verbose_name = 'Сотрудник'
#        verbose_name_plural = 'Сотрудники'


class Rank(models.Model):
    name = models.CharField(max_length=50, verbose_name='Звание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'


class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Subdivision(models.Model):
    name = models.CharField(max_length=50, verbose_name='Подразделение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Researched_objects(models.Model ):
    name = models.CharField(max_length=50, verbose_name='Название')
    type_objects = models.ForeignKey('Type_Objects', on_delete=models.PROTECT, verbose_name='Тип объекта')
    serial_number = models.CharField(max_length=50, verbose_name='Серийный номер')
    images1 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото1', blank=True)
    images2 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото2', blank=True)
    images3 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото3', blank=True)
    additional_information = models.TextField(blank=True, verbose_name='Дополнительные сведения')

    def get_absolute_url(self):
        return reverse('researched_objects', kwargs={'researched_objects_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Type_Objects(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип объекта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Типы объектов'

class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


