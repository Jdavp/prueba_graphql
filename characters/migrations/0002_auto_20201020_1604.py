# Generated by Django 3.1.2 on 2020-10-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('opening_crawl', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='films',
            name='planets',
        ),
        migrations.RenameModel(
            old_name='Planets',
            new_name='Planet',
        ),
        migrations.DeleteModel(
            name='Characters',
        ),
        migrations.DeleteModel(
            name='Films',
        ),
        migrations.AddField(
            model_name='film',
            name='planets',
            field=models.ManyToManyField(related_name='planet', to='characters.Planet'),
        ),
        migrations.AddField(
            model_name='character',
            name='films',
            field=models.ManyToManyField(related_name='film', to='characters.Film'),
        ),
    ]
