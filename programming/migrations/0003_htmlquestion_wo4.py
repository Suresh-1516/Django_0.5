# Generated by Django 4.1.7 on 2023-04-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programming', '0002_htmlquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='htmlquestion',
            name='wo4',
            field=models.CharField(default='', max_length=20),
        ),
    ]