# Generated by Django 5.0.4 on 2024-04-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_recipe_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipeTitle', models.CharField(max_length=100, null=True)),
                ('ingredients', models.CharField(max_length=100, null=True)),
                ('instructions', models.CharField(max_length=100, null=True)),
                ('preparationTime', models.CharField(max_length=100, null=True)),
                ('cookingTime', models.CharField(max_length=100, null=True)),
                ('totalTime', models.CharField(max_length=100, null=True)),
                ('nutritionalInfo', models.CharField(max_length=100, null=True)),
                ('difficultyLevel', models.CharField(max_length=100, null=True)),
                ('recipe_type', models.CharField(max_length=100, null=True)),
                ('Tag_type', models.CharField(max_length=100, null=True)),
                ('totalCalories', models.CharField(max_length=100, null=True)),
                ('recipeImage', models.ImageField(null=True, upload_to='static/media')),
            ],
        ),
    ]
