# Generated by Django 4.1.3 on 2022-11-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='college_name',
            field=models.CharField(default='IIT BHU', max_length=100),
        ),
    ]