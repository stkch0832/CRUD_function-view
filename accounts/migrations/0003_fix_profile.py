# Generated by Django 3.2.14 on 2023-03-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_add_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='introduction',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
