# Generated by Django 4.0.2 on 2022-03-26 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='closing_date',
            field=models.DateTimeField(default='2022-03-26 13:00:00.000Z'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='issue',
            field=models.CharField(default='issue', max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='science',
            field=models.CharField(default='science', max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.CharField(default='tools', max_length=600),
            preserve_default=False,
        ),
    ]
