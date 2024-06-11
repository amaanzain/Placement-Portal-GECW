# Generated by Django 5.0.2 on 2024-03-22 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('batch', models.IntegerField()),
                ('github', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('experience', models.TextField(max_length=3500)),
            ],
        ),
    ]