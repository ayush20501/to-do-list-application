# Generated by Django 5.0.1 on 2024-02-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]