# Generated by Django 2.1.3 on 2019-01-29 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
        ('groups', '0007_auto_20190129_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servers.Server'),
        ),
    ]
