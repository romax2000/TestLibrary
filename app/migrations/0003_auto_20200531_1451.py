# Generated by Django 3.0.6 on 2020-05-31 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_book_reader'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['book_name']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['full_name']},
        ),
        migrations.AlterField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
