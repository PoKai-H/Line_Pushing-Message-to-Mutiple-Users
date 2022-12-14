# Generated by Django 4.0.5 on 2022-07-01 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(max_length=100)),
                ('message_push', models.CharField(max_length=200)),
                ('group_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Message.group')),
            ],
        ),
    ]
