# Generated by Django 4.2.7 on 2024-01-01 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tematy', '0002_wpisy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wpisy',
            options={'verbose_name_plural': 'wpisy'},
        ),
        migrations.AddField(
            model_name='tematy',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
