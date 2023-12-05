# Generated by Django 3.2.23 on 2023-12-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='recipe_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]