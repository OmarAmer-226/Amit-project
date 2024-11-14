# Generated by Django 5.0 on 2024-11-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_maindishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='/path/to/default/image.png', null=True, upload_to='')),
            ],
        ),
    ]
