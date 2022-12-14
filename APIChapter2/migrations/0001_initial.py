# Generated by Django 4.1.3 on 2022-11-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50)),
                ('Address', models.TextField(blank=True, max_length=500)),
                ('City', models.CharField(blank=True, max_length=50)),
                ('State', models.CharField(blank=True, max_length=20)),
                ('Mobile', models.IntegerField(blank=True, max_length=50)),
                ('EmailId', models.EmailField(blank=True, max_length=50)),
                ('Password', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50)),
                ('Address', models.TextField(blank=True, max_length=500)),
                ('City', models.CharField(blank=True, max_length=50)),
                ('State', models.CharField(blank=True, max_length=20)),
                ('Mobile', models.IntegerField(blank=True, max_length=50)),
                ('EmailId', models.EmailField(blank=True, max_length=50)),
                ('Password', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
