# Generated by Django 5.1.3 on 2024-12-06 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_education_personaldetails_skill_workexperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='phone',
            field=models.CharField(default='0000000000', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(max_length=100),
        ),
    ]
