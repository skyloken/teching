# Generated by Django 2.2.1 on 2019-05-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190507_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='app.Tag', verbose_name='タグ'),
        ),
    ]