# Generated by Django 3.2.5 on 2021-07-15 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_comment_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Trail Name'),
        ),
    ]
