# Generated by Django 4.2.1 on 2023-05-18 17:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, validators=[events.models.titleValidator])),
                ('description', models.TextField()),
                ('eventImage', models.ImageField(blank=True, upload_to='images/')),
                ('category', models.CharField(choices=[('Music', 'Music'), ('Cinema', 'Cinema'), ('Sport', 'Sport')], max_length=8)),
                ('state', models.BooleanField(default=False)),
                ('nbr_Participant', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Number of participant must be positive')])),
                ('eventDate', models.DateField(validators=[events.models.dateValidators])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePart', models.DateField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
