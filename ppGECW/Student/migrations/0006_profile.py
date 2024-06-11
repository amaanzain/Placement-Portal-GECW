# Generated by Django 5.0.2 on 2024-02-22 04:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_alter_placementdetails_ctc'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, default='default_profile_pic.png', upload_to='profile_pics/')),
                ('cgpa', models.FloatField(blank=True, null=True)),
                ('batch', models.CharField(blank=True, max_length=20, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
