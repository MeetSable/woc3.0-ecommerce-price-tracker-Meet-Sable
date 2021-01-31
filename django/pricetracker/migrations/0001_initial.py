# Generated by Django 3.1.5 on 2021-01-26 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Enter Your Name', max_length=30)),
                ('emailaddress', models.EmailField(max_length=254)),
                ('password', models.CharField(help_text='Enter password', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(max_length=1000)),
                ('desired_price', models.FloatField()),
                ('current_price', models.FloatField()),
                ('desired_price_on_site', models.BooleanField()),
                ('product_name', models.CharField(max_length=200)),
                ('site_name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricetracker.user')),
            ],
        ),
    ]