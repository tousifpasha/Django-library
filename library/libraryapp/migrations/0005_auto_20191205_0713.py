# Generated by Django 2.2.7 on 2019-12-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0004_auto_20191118_0403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'author'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'book'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'category'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name_plural': 'member'},
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name_plural': 'record'},
        ),
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(help_text='Enter the author name', max_length=100, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(help_text='Enter the books category', max_length=100, verbose_name='category'),
        ),
    ]
