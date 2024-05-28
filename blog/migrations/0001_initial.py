# Generated by Django 4.2.8 on 2024-05-27 06:43

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=500, primary_key=True, serialize=False, unique=True)),
                ('meta_description', models.CharField(default='meta description', max_length=160)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('post_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('comments_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
