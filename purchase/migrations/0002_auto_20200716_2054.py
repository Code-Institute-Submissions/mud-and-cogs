# Generated by Django 3.0.7 on 2020-07-16 20:54

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasepart',
            old_name='purchasepart_total',
            new_name='total',
        ),
        migrations.AddField(
            model_name='purchase',
            name='country',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='original_basket',
            field=models.TextField(default=''),
        ),
    ]
