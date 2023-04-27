# Generated by Django 4.2 on 2023-04-27 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Fit_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gramme', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('calories', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('carbohydrates', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fit_website.ingredient')),
            ],
        ),
        migrations.RemoveField(
            model_name='meal',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='quantity',
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.AddField(
            model_name='ingredientquantity',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fit_website.meal'),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(through='Fit_website.IngredientQuantity', to='Fit_website.ingredient'),
        ),
    ]
