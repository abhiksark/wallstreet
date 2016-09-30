# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-30 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellbuy', '0008_auto_20160929_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='queries',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='ACME',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Ammunation_Pharma',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Bajrang_Cafe',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Bakers_Street_Findings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Buzzinga_Entertainment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Daily_Planet',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Evil_Inc',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Gringotts_Bank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Hammer_Tech',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Illuminati_Consolidations',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='LexCorp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Monsters_Inc',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Olivanders_Wand',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Oscorp_RnD',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Palmer_Tech',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Pearson_Hardman',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='SHIELD',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='STAR_Labs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Skynet',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Stark_Industries',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Umbrella_Corp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Walter_White_Inc',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Wayne_Enterprises',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='Xaviers_School',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='id',
            field=models.IntegerField(primary_key='True', serialize=False),
        ),
        migrations.AlterField(
            model_name='sharedetail',
            name='money_in_hand',
            field=models.DecimalField(decimal_places=2, default=100000.0, max_digits=14),
        ),
        migrations.AlterField(
            model_name='timer',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
