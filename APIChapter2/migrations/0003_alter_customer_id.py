# Generated by Django 4.1.3 on 2022-11-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIChapter2', '0002_alter_customer_emailid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.IntegerField(blank=True, max_length=50, primary_key=True, serialize=False),
        ),
    ]
