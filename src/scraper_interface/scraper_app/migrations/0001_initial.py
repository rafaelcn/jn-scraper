# Generated by Django 2.2 on 2019-04-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('imgs', models.CharField(max_length=400)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]