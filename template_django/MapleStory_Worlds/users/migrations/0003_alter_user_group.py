# Generated by Django 4.1 on 2022-09-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_group_alter_user_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="group",
            field=models.CharField(
                choices=[
                    ("NONE", "NONE"),
                    ("D", "D"),
                    ("C", "C"),
                    ("B", "B"),
                    ("A", "A"),
                ],
                max_length=6,
                null=True,
                verbose_name="그룹",
            ),
        ),
    ]
