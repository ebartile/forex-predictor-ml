# Generated by Django 2.1.5 on 2019-06-10 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=255)),
                ('feed_url', models.CharField(max_length=255)),
                ('published_date', models.DateTimeField()),
                ('created_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'stories',
            },
        ),
    ]
