# Generated by Django 3.1.3 on 2020-12-14 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20201212_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.RemoveField(
            model_name='work',
            name='slug',
        ),
    ]