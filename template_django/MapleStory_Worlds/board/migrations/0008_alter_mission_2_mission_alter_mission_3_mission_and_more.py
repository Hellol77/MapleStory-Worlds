# Generated by Django 4.1 on 2022-09-09 13:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0007_mission_1_end_date_mission_2_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mission_2",
            name="mission",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mission_3",
            name="mission",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mission_4",
            name="mission",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mission_5",
            name="mission",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]