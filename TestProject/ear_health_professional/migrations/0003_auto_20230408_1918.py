# Generated by Django 3.1 on 2023-04-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ear_health_professional', '0002_rating_review_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_professional_account',
            name='Health_Professional_Image',
            field=models.ImageField(default='dummyprofile.jpg', upload_to='Health_Professional/'),
        ),
    ]
