# Generated by Django 4.2.7 on 2023-12-03 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tematy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wpisy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('temat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tematy.tematy')),
            ],
        ),
    ]
