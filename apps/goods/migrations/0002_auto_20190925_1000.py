# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-25 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_to_goods', to='goods.Goods', verbose_name='商品'),
        ),
    ]
