# Generated by Django 4.0.4 on 2022-08-08 01:06
#pbkdf2_sha256$320000$K2OUREfyA4VC0QmwzFKKZ3$E92wz+LLZxEZK/TMtOOEp5LGb4QHhw1AIJUZutfA09M=
#pbkdf2_sha256$320000$wcyMkplVhklc1XpvMNFBhU$q0L9T7fpkz7q8RbzdC3XPpRQgqjdjq2iBe6vY0risP8=
from django.conf import settings
from django.contrib.auth.models import User
from django.db import migrations
def add_user(apps, schema_editor):
    user = User.objects.create_user('admin', 'admin@mail.com', '123')
    user.is_superuser = 1
    user.is_staff = 1
    user.first_name = 'Andres'
    user.last_name = 'Rodriguez'
    user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('ventasApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_user),
    ]
