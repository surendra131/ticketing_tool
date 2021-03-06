# Generated by Django 3.2.6 on 2021-08-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0003_alter_issue_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignee',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='estimated_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='labels',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='logged_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='watchers',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
