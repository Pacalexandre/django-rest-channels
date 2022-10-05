# Generated by Django 4.0.6 on 2022-07-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processo', models.CharField(max_length=20)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]