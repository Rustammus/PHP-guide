# Generated by Django 4.1.5 on 2023-01-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_datademand_верхний html_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datamain",
            name="html_bot",
            field=models.FileField(default=None, null=True, upload_to="file/main/"),
        ),
        migrations.AlterField(
            model_name="datamain",
            name="html_top",
            field=models.FileField(default=None, null=True, upload_to="file/main/"),
        ),
        migrations.AlterField(
            model_name="datamain",
            name="pic_center",
            field=models.ImageField(
                default=None, null=True, upload_to="pictures/main/"
            ),
        ),
    ]
