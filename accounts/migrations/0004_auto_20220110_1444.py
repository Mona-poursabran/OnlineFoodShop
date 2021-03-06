# Generated by Django 3.2.9 on 2022-01-10 11:14

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220109_1619'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResturantManager',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.CreateModel(
            name='ResturantManager',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.customuser')),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
            },
            bases=('accounts.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
