# Generated by Django 3.2.9 on 2022-01-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20220120_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='branch/%Y__%m__%d/'),
        ),
    ]
