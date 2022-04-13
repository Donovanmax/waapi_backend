# Generated by Django 3.2.7 on 2022-04-08 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_account_external_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='uploads/business/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='uploads/business/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='uploads/business/')),
            ],
        ),
        migrations.RenameField(
            model_name='business',
            old_name='category',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='favoris',
        ),
        migrations.AddField(
            model_name='business',
            name='arrondissement',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='business',
            name='email',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='quartier',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='business',
            name='website',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='tested',
            field=models.ManyToManyField(blank=True, related_name='vu', to='business.Account'),
        ),
        migrations.AlterField(
            model_name='business',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comment', to='business.Comment'),
        ),
        migrations.RemoveField(
            model_name='business',
            name='to_be_visited',
        ),
        migrations.AddField(
            model_name='business',
            name='to_be_visited',
            field=models.ManyToManyField(blank=True, related_name='favourites', to='business.Account'),
        ),
        migrations.RemoveField(
            model_name='business',
            name='visited',
        ),
        migrations.AddField(
            model_name='business',
            name='visited',
            field=models.ManyToManyField(blank=True, related_name='visitors', to='business.Account'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='business',
            name='carousel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carousel_img', to='business.images'),
        ),
    ]