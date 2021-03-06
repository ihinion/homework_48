# Generated by Django 2.2 on 2020-08-30 14:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200731_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Amount')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.Product', verbose_name='Cart')),
            ],
        ),
    ]
