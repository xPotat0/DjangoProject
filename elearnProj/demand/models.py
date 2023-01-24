from django.db import models


class Index(models.Model):
    is_black = [('b', 'Черное'), ('w', 'Белое')]

    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()
    list = models.BooleanField(default=False)
    li_num = models.IntegerField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="photos/%Y/%m/%d/")
    back = models.CharField(default='w', choices=is_black, max_length=255)
    hrefer = models.CharField(max_length=255, default='#')
    icon_image = models.ImageField(blank=True, null=True, upload_to="photos/%Y/%m/%d/")

    class Meta:
        verbose_name = "Стартовая страница"
        verbose_name_plural = "Стартовая страница"


class Skills(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    year = models.CharField(max_length=255, default=1970)

    class Meta:
        verbose_name = "Умения"
        verbose_name_plural = "Умения"
        ordering = ['-amount',]

class Demand(models.Model):
    choice = [('va', 'Кол-во вакансий'), ('sl', 'Уровень зарплат'), ('vad', 'Кол-во вакансий GameDev'), ('sld', 'Уровень зарплат GameDev')]

    year = models.CharField(max_length=255)
    salary_amount = models.IntegerField()
    type = models.CharField(max_length=255, choices=choice, default='va')

    class Meta:
        verbose_name = "Востребованность"
        verbose_name_plural = "Востребованности"


class Geography(models.Model):
    choice = [('sal', 'Зарплата'), ('amo', 'Кол-во')]

    city = models.CharField(max_length=255)
    salary_amount = models.IntegerField()
    type = models.CharField(max_length=255, choices=choice, default='sal')

    class Meta:
        verbose_name = 'География'
        verbose_name_plural = 'География'