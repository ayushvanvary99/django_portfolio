# Generated by Django 4.1 on 2024-05-08 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webpage", "0007_alter_projects_proj_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="photo",
            field=models.ImageField(upload_to="media/projects/%Y/"),
        ),
    ]