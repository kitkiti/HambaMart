# Generated by Django 5.1.1 on 2024-09-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
