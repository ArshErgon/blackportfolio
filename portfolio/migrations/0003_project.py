# Generated by Django 3.0.3 on 2020-05-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_delete_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_image', models.CharField(max_length=250)),
                ('project_name', models.CharField(max_length=100)),
                ('project_body', models.TextField()),
            ],
        ),
    ]
