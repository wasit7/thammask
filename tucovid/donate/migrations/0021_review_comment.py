# Generated by Django 3.0.4 on 2020-04-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0020_auto_20200403_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
