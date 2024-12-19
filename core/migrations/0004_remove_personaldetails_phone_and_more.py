# Generated by Django 5.1.3 on 2024-12-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_personaldetails_phone_alter_education_degree_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetails',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='personaldetails',
            name='website',
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
    ]
