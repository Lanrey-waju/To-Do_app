# Generated by Django 4.0a1 on 2021-10-27 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_todolist_options_todolist_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='task_description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]