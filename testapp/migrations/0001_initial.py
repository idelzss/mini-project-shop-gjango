# Generated by Django 5.2 on 2025-06-29 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('page', models.PositiveIntegerField()),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=50)),
                ('year_of_birth', models.DateField(verbose_name='Date of birth')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='testapp.book')),
            ],
        ),
    ]
