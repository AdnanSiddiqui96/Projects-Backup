# Generated by Django 4.1.2 on 2023-06-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_loan_account_id_alter_account_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[('approved', 'approved'), ('rejected', 'rejected'), ('pending', 'pending')], default='pending', max_length=255),
        ),
    ]