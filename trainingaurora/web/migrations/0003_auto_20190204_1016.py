# Generated by Django 2.0.1 on 2019-02-04 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190204_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='destination',
            field=models.ForeignKey(blank=True, help_text='desitnation tour to destination table', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='web.City', verbose_name='destination'),
        ),
    ]