# Generated by Django 3.0.3 on 2020-05-05 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('quora', models.CharField(max_length=100)),
                ('github', models.CharField(max_length=100)),
            ],
        ),
    ]