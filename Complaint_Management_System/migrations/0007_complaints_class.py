# Generated by Django 4.0.5 on 2022-08-05 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complaint_Management_System', '0006_complaints_imageproof'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='Class',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
