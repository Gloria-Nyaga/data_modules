# Generated by Django 5.0.6 on 2024-06-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_capacity', models.PositiveSmallIntegerField()),
                ('class_schedule', models.TextField()),
                ('class_attendance', models.PositiveSmallIntegerField()),
                ('class_projects', models.TextField()),
                ('class_activities', models.TextField()),
                ('class_representatives', models.TextField()),
                ('class_assignments', models.TextField()),
                ('class_policies', models.TextField()),
                ('class_requirements', models.TextField()),
                ('class_members_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
