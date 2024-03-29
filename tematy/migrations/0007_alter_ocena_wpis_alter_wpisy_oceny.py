# Generated by Django 4.2.7 on 2024-01-02 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tematy', '0006_alter_tematy_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocena',
            name='wpis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oceny_wpisy', to='tematy.wpisy'),
        ),
        migrations.AlterField(
            model_name='wpisy',
            name='oceny',
            field=models.ManyToManyField(related_name='wpisy_oceny', to='tematy.ocena'),
        ),
    ]
