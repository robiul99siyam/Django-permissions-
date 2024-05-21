# Generated by Django 5.0.6 on 2024-05-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
    ]
