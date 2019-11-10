# Generated by Django 3.0b1 on 2019-11-10 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Szöveg')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Létrehozás dátuma')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Megjegyzés')),
            ],
            options={
                'verbose_name': 'Megjegyzés',
                'verbose_name_plural': 'Megjegyzések',
            },
        ),
    ]