# Generated by Django 2.2.5 on 2020-01-09 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191014_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_crud_author', 'CRUD author'),)},
        ),
    ]
