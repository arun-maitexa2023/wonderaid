# Generated by Django 3.2.8 on 2023-07-15 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelaid', '0005_packegetravels'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packegetravels',
            old_name='travels',
            new_name='Travels',
        ),
        migrations.CreateModel(
            name='Chatcommunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Communityname', models.CharField(max_length=50)),
                ('Chat', models.CharField(max_length=50)),
                ('Createdtime', models.CharField(max_length=50)),
                ('Uploaddate', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.user')),
            ],
        ),
    ]
