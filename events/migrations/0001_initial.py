# Generated by Django 5.1.3 on 2024-11-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('interest', models.CharField(choices=[('software-development', 'Software Development'), ('cybersecurity', 'Cybersecurity'), ('data-science', 'Data Science'), ('ai', 'Artificial Intelligence')], max_length=50)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]