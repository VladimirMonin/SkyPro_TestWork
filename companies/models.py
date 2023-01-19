from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта',
                            max_length=50)

    model = models.CharField(verbose_name='Модель продукта',
                             max_length=100)

    release_date = models.DateField(verbose_name='Дата выхода на рынок',
                                    auto_now=False,
                                    auto_now_add=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Company(models.Model):
    TYPES = (
        (0, 'Завод'),
        (1, 'Дистрибьютер'),
        (2, 'Диллерский центр'),
        (3, 'Крупная розничная сеть'),
        (4, 'Индивидуальный предприниматель')
    )

    hierarchy = models.SmallIntegerField(
        verbose_name='Тип компании',
        choices=TYPES)

    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name='Тип компании')

    email = models.EmailField(max_length=100,
                              unique=True)

    country = models.CharField(verbose_name='Название страны',
                               max_length=25)

    city = models.CharField(verbose_name='Название города',
                            max_length=25)

    street = models.CharField(verbose_name='Название улицы',
                              max_length=50)

    building = models.CharField(verbose_name='Номер дома и офис',
                                max_length=25)

    products = models.ManyToManyField(Product,
                                      related_name='companies')

    provider = models.ForeignKey('self',
                                 on_delete=models.SET_NULL,
                                 verbose_name='Поставщик',
                                 related_name='traders',
                                 null=True,
                                 blank=True)

    debt = models.DecimalField(max_digits=20,
                               decimal_places=2,
                               verbose_name='Задолженность',
                               default=0)

    pub_data = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name
