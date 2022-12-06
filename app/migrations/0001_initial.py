# Generated by Django 4.0.2 on 2022-12-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, verbose_name='вопрос')),
                ('score', models.PositiveIntegerField(verbose_name='балл')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, verbose_name='ответ')),
                ('score', models.PositiveIntegerField(verbose_name='балл')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, verbose_name='вопрос')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_score', models.PositiveIntegerField(verbose_name='от')),
                ('max_score', models.PositiveIntegerField(verbose_name='до')),
                ('recommendation', models.TextField(verbose_name='рекомендация')),
            ],
        ),
    ]