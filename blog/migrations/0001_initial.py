# Generated by Django 3.0rc1 on 2019-11-30 15:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Cím')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Szöveg')),
                ('image', models.ImageField(blank=True, upload_to='blog/cover_images/', verbose_name='Borítókép')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Létrehozás dátuma')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Utolsó módosítás dátuma')),
                ('slug', models.SlugField(unique=True, verbose_name='Link cím')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Író')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Post')),
                ('published', models.BooleanField(default=True, verbose_name='Közzétett állapot')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Kezdeti dátum és idő')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Befejezési dátum és idő')),
            ],
            options={
                'verbose_name': 'Esemény',
                'verbose_name_plural': 'Események',
            },
            bases=('blog.post',),
        ),
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
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Post')),
                ('published', models.BooleanField(default=True, verbose_name='Közzétett állapot')),
                ('related', models.ManyToManyField(blank=True, related_name='_announcement_related_+', to='blog.Announcement', verbose_name='Kapcsolódó bejegyzések')),
            ],
            options={
                'verbose_name': 'Közlemény',
                'verbose_name_plural': 'Közlemények',
            },
            bases=('blog.post',),
        ),
    ]
