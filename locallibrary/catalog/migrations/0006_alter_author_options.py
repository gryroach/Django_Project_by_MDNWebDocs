# Generated by Django 3.2.8 on 2021-11-09 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name'], 'permissions': (('can_change', 'Create, update or delete authors'),)},
        ),
    ]
