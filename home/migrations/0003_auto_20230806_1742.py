# Generated by Django 3.2.18 on 2023-08-06 16:42

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_reviews_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated',
        ),
    ]