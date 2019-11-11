# Generated by Django 2.2.7 on 2019-11-07 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('establish_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('roll', models.CharField(max_length=6)),
                ('registration_number', models.CharField(max_length=6)),
                ('semester', models.CharField(default='1st', max_length=3)),
                ('mobile', models.CharField(max_length=11)),
                ('guardian_mobile', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('last_gpa', models.FloatField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Department')),
            ],
        ),
    ]