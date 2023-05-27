# Generated by Django 4.1.7 on 2023-04-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programming', '0006_alter_payment_amount_alter_payment_mobile_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_user', models.CharField(default=None, max_length=50)),
                ('note_1', models.CharField(default=None, max_length=400)),
                ('note_2', models.CharField(default=None, max_length=400)),
                ('note_3', models.CharField(default=None, max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_content',
            field=models.CharField(default='', max_length=800),
        ),
    ]