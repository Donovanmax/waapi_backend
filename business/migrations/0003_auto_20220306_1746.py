# Generated by Django 3.2.7 on 2022-03-06 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20220306_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='business.Account'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_owner', to='business.account'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.account'),
        ),
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='Like', max_length=10),
        ),
    ]
