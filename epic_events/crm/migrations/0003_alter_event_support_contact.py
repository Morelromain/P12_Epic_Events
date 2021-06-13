# Generated by Django 3.2.3 on 2021-06-12 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'Support'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]