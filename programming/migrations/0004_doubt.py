# Generated by Django 4.1.7 on 2023-04-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programming', '0003_htmlquestion_wo4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubt_user', models.CharField(default='', max_length=20)),
                ('doubt_lang', models.CharField(default='', max_length=50)),
                ('doubt_q', models.CharField(default='', max_length=30)),
                ('doubt_code', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
