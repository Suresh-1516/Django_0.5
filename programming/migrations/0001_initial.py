# Generated by Django 4.1.7 on 2023-04-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=20)),
                ('premium_name', models.CharField(default='Nope', max_length=20)),
                ('order_id', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='Nope', max_length=254)),
                ('amount', models.IntegerField(default=0)),
                ('mobileno', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium_name', models.CharField(default='', max_length=20)),
                ('premium_amount', models.IntegerField(default=0)),
                ('premium_img', models.ImageField(default='', upload_to='premium/images')),
                ('premium_date', models.DateField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Save_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_user', models.CharField(default='', max_length=100)),
                ('file_name', models.CharField(max_length=20)),
                ('file_date', models.DateField()),
                ('file_content', models.TextField(max_length=1000)),
            ],
        ),
    ]