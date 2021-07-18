# Generated by Django 3.2.5 on 2021-07-18 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
        ("photos", "0002_photo_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="posts.post",
            ),
        ),
        migrations.AlterField(
            model_name="photo",
            name="temp_file",
            field=models.FileField(null=True, upload_to="uploads/"),
        ),
    ]