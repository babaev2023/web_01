# Generated by Django 4.2.3 on 2023-07-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.CharField(max_length=100, verbose_name='Тип')),
                ('contact', models.EmailField(max_length=254, verbose_name='Почта')),
                ('full_text_incident', models.TextField(verbose_name='Детали инцидента')),
                ('date', models.DateTimeField(verbose_name='Дата инцидента')),
            ],
            options={
                'verbose_name': 'Инцидент',
                'verbose_name_plural': 'Инциденты',
            },
        ),
    ]
