# Generated by Django 5.0.4 on 2024-08-04 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0027_justifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='filieres',
        ),
        migrations.AddField(
            model_name='cours',
            name='filieres',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cours', to='site1.filiere'),
        ),
    ]
