from django.db import models

class Incidents(models.Model):
        tip = models.CharField('Тип', max_length=100)
        contact = models.EmailField('Почта')
        full_text_incident = models.TextField('Детали инцидента')
        date = models.DateTimeField('Дата инцидента')


        def __str__(self):
            return self.tip

        class Meta:
                verbose_name = 'Инцидент'
                verbose_name_plural = 'Инциденты'
