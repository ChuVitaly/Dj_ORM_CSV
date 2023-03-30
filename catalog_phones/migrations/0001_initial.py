# Generated by Django 4.1.7 on 2023-03-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('image', models.URLField(max_length=300)),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(null=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]