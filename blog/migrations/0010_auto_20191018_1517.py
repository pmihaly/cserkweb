# Generated by Django 3.0b1 on 2019-10-18 15:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191018_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bejegyzes',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Szöveg'),
        ),
    ]
