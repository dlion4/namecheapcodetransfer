# Generated by Django 4.2.5 on 2023-11-14 03:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_post_is_premium"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=180),
        ),
    ]
