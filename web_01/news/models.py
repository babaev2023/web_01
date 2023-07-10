from django.db import models

class Articles(models.Model):
        title = models.CharField('Название', max_length=200)
        anons = models.CharField('Анонс', max_length=250)
        full_text = models.TextField('Новость')
        date = models.DateTimeField('Дата публикации')

        def __str__(self):
            return self.title

        class Meta:
                verbose_name = 'Новость'
                verbose_name_plural = 'Новости'