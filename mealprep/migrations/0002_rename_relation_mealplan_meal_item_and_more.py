# Generated by Django 4.1 on 2022-08-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealprep', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mealplan',
            old_name='relation',
            new_name='meal_item',
        ),
        migrations.RemoveField(
            model_name='mealplan',
            name='meal',
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
