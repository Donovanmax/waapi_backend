# Generated by Django 3.2.7 on 2022-04-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_auto_20220408_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='businessName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
