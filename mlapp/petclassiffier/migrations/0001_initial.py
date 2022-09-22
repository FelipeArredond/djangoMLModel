# Generated by Django 4.1.1 on 2022-09-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mlModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('architecture', models.FileField(upload_to='../../ml_model')),
                ('weigths', models.FileField(upload_to='../../ml_model')),
                ('priority', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
    ]
