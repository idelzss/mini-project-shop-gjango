# Generated by Django 5.2 on 2025-06-29 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library_literature',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField(help_text='Write a short description of the book.')),
                ('genre', models.CharField()),
                ('publication_date', models.DateField()),
                ('author', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_Cart',
            fields=[
                ('number_cart', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_issue', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('specialty', models.CharField(max_length=70)),
                ('student_card_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='university_homework.student_cart')),
            ],
        ),
        migrations.CreateModel(
            name='Process_of_taking_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_giving', models.DateField()),
                ('full_name_issued', models.CharField()),
                ('literature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='literatures', to='university_homework.library_literature')),
                ('taker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_taker', to='university_homework.student_cart')),
            ],
        ),
        migrations.CreateModel(
            name='Student_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=25)),
                ('group_slogan', models.TextField()),
                ('meeting_group', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_group', to='university_homework.student', verbose_name='students')),
            ],
        ),
    ]
