# Generated by Django 4.0.6 on 2022-08-06 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_text',
            field=models.CharField(default='task', max_length=500),
        ),
    ]
