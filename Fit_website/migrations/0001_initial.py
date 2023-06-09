# Generated by Django 4.2 on 2023-04-27 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gramme', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('calories', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('carbohydrates', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ingredient', models.ManyToManyField(to='Fit_website.ingredients')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeofDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Śniadanie', 'Śniadanie'), ('Obiad', 'Obiad'), ('Kolacja', 'Kolacja')])),
            ],
        ),
        migrations.CreateModel(
            name='MealTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Poniedziałek', 'Poniedziałek'), ('Wtorek', 'Wtorek'), ('Środa', 'Środa'), ('Czwartek', 'Czwartek'), ('Piątek', 'Piątek'), ('Sobota', 'Sobota'), ('Niedziela', 'Niedziela')])),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fit_website.meal')),
                ('timeofday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fit_website.timeofday')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
