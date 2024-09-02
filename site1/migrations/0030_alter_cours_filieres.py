# Generated by Django 5.0.4 on 2024-08-04 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0029_alter_cours_filieres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='filieres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cours', to='site1.filiere'),
        ),
    ]
