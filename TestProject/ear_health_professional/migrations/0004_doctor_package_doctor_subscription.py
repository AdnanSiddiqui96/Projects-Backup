# Generated by Django 4.2.1 on 2023-06-03 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ear_health_professional', '0003_auto_20230408_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Package',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('duration', models.IntegerField(default=0)),
                ('type', models.CharField(default='', max_length=50)),
                ('price', models.FloatField(default=0, max_length=55)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0, max_length=55)),
                ('payid', models.CharField(default='', max_length=50)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctorsubscription', to='ear_health_professional.health_professional_account')),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctorpackage', to='ear_health_professional.doctor_package')),
            ],
        ),
    ]
