# Generated by Django 4.1.1 on 2022-09-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
