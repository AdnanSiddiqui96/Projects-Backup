# Generated by Django 4.1.2 on 2023-06-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_loan_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='block',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('rejected', 'rejected'), ('approved', 'approved')], default='pending', max_length=255),
        ),
    ]