# Generated by Django 3.2.8 on 2021-10-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_comment_comment_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
