# Generated by Django 3.2.8 on 2023-07-14 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50, unique=True)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('userdob', models.CharField(max_length=50, null=True)),
                ('usergender', models.CharField(max_length=50, null=True)),
                ('userphone', models.CharField(max_length=50)),
                ('usermail', models.CharField(max_length=50)),
                ('userplace', models.CharField(max_length=50, null=True)),
                ('userpincode', models.CharField(max_length=50, null=True)),
                ('userpassword', models.CharField(max_length=50)),
                ('userdp', models.ImageField(null=True, upload_to='images/')),
                ('role', models.CharField(max_length=50)),
                ('userstatus', models.CharField(max_length=50)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.log')),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patrons', models.CharField(max_length=50)),
                ('Average', models.CharField(max_length=50)),
                ('Solo', models.CharField(max_length=50)),
                ('Leadingcommunity', models.CharField(max_length=50, null=True)),
                ('Includingcommunity', models.CharField(max_length=50, null=True)),
                ('Nextdestination', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50)),
                ('Userprofile_status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.user')),
            ],
        ),
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelsname', models.CharField(max_length=50)),
                ('travelsphone', models.CharField(max_length=50)),
                ('travelsmail', models.CharField(max_length=50)),
                ('travelslocation', models.CharField(max_length=50, null=True)),
                ('travelspincode', models.CharField(max_length=50, null=True)),
                ('travelsrating', models.CharField(max_length=50, null=True)),
                ('travelspackages', models.CharField(max_length=50, null=True)),
                ('travelstiming', models.CharField(max_length=50, null=True)),
                ('travelspass', models.CharField(max_length=50, null=True)),
                ('policies', models.CharField(max_length=50, null=True)),
                ('reviews', models.CharField(max_length=50, null=True)),
                ('images', models.ImageField(null=True, upload_to='images/')),
                ('role', models.CharField(max_length=50)),
                ('travelsstatus', models.CharField(max_length=50)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.log')),
            ],
        ),
        migrations.CreateModel(
            name='Spots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Spotsname', models.CharField(max_length=50)),
                ('Spotsclimat', models.CharField(max_length=50)),
                ('Bestperiod', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50, null=True)),
                ('Visiterscount', models.CharField(max_length=50, null=True)),
                ('Rating', models.CharField(max_length=50, null=True)),
                ('Area', models.CharField(max_length=50, null=True)),
                ('View', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50)),
                ('Spots_status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.user')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurentname', models.CharField(max_length=50)),
                ('restaurentphone', models.CharField(max_length=50)),
                ('restaurentmail', models.CharField(max_length=50)),
                ('restaurentlocation', models.CharField(max_length=50, null=True)),
                ('restaurentpin', models.CharField(max_length=50, null=True)),
                ('restaurentrating', models.CharField(max_length=50, null=True)),
                ('restaurentcategory', models.CharField(max_length=50, null=True)),
                ('restaurentmenu', models.CharField(max_length=50, null=True)),
                ('specialoffers', models.CharField(max_length=50, null=True)),
                ('specials', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('nba', models.CharField(max_length=50, null=True)),
                ('policies', models.CharField(max_length=50, null=True)),
                ('diningoptions', models.CharField(max_length=50, null=True)),
                ('restaurenttiming', models.CharField(max_length=50, null=True)),
                ('restaurentpass', models.CharField(max_length=50)),
                ('reviews', models.CharField(max_length=50, null=True)),
                ('images', models.ImageField(null=True, upload_to='images/')),
                ('role', models.CharField(max_length=50)),
                ('Restaurentstatus', models.CharField(max_length=50)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.log')),
            ],
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resortname', models.CharField(max_length=50)),
                ('resortphone', models.CharField(max_length=50)),
                ('resortmail', models.CharField(max_length=50)),
                ('resortlocation', models.CharField(max_length=50, null=True)),
                ('resortpincode', models.CharField(max_length=50, null=True)),
                ('resortrating', models.CharField(max_length=50, null=True)),
                ('resortrooms', models.CharField(max_length=50, null=True)),
                ('resortcategory', models.CharField(max_length=50, null=True)),
                ('resortpackages', models.CharField(max_length=50, null=True)),
                ('resortservices', models.CharField(max_length=50, null=True)),
                ('resortfecilities', models.CharField(max_length=50, null=True)),
                ('resorttiming', models.CharField(max_length=50, null=True)),
                ('specialoffers', models.CharField(max_length=50, null=True)),
                ('availability', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('nba', models.CharField(max_length=50, null=True)),
                ('policies', models.CharField(max_length=50, null=True)),
                ('accomodationtypes', models.CharField(max_length=50, null=True)),
                ('accomodationdesc', models.CharField(max_length=50, null=True)),
                ('foodmenu', models.CharField(max_length=50, null=True)),
                ('diningoptions', models.CharField(max_length=50, null=True)),
                ('pricing', models.CharField(max_length=50, null=True)),
                ('reviews', models.CharField(max_length=50, null=True)),
                ('images', models.ImageField(null=True, upload_to='images/')),
                ('resortpass', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('resortstatus', models.CharField(max_length=50)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.log')),
            ],
        ),
        migrations.CreateModel(
            name='Plannedtrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Startingpoint', models.CharField(max_length=50)),
                ('Destination', models.CharField(max_length=50)),
                ('Days', models.CharField(max_length=50)),
                ('Nights', models.CharField(max_length=50)),
                ('Plan', models.CharField(max_length=50, null=True)),
                ('Guide', models.CharField(max_length=50, null=True)),
                ('Travels', models.CharField(max_length=50, null=True)),
                ('Persons', models.CharField(max_length=50, null=True)),
                ('Budget', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50)),
                ('Plannedtrip_status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.user')),
            ],
        ),
        migrations.CreateModel(
            name='Packege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Packegename', models.CharField(max_length=50)),
                ('Destination', models.CharField(max_length=50)),
                ('Price', models.CharField(max_length=50)),
                ('Startdate', models.CharField(max_length=50)),
                ('Enddate', models.CharField(max_length=50)),
                ('Bookingcount', models.CharField(max_length=50)),
                ('Packegestatus', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.user')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sender', models.CharField(max_length=50)),
                ('Receiver', models.CharField(max_length=50)),
                ('Notification', models.CharField(max_length=50)),
                ('Date', models.CharField(max_length=50)),
                ('Action', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50)),
                ('Notificationstatus', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.user')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=50)),
                ('hotelphone', models.CharField(max_length=50)),
                ('hotelmail', models.CharField(max_length=50)),
                ('hotellocation', models.CharField(max_length=50, null=True)),
                ('hotelpincode', models.CharField(max_length=50, null=True)),
                ('hotelrating', models.CharField(max_length=50, null=True)),
                ('hotelrooms', models.CharField(max_length=50, null=True)),
                ('hotelcategory', models.CharField(max_length=50, null=True)),
                ('hotelfecilities', models.CharField(max_length=50, null=True)),
                ('hotelpackages', models.CharField(max_length=50, null=True)),
                ('hotelservices', models.CharField(max_length=50, null=True)),
                ('hoteltiming', models.CharField(max_length=50, null=True)),
                ('specialoffers', models.CharField(max_length=50, null=True)),
                ('roomsavailability', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('nba', models.CharField(max_length=50, null=True)),
                ('policies', models.CharField(max_length=50, null=True)),
                ('hotelpass', models.CharField(max_length=50)),
                ('menu', models.CharField(max_length=50, null=True)),
                ('reviews', models.CharField(max_length=50, null=True)),
                ('images', models.ImageField(null=True, upload_to='images/')),
                ('role', models.CharField(max_length=50)),
                ('hotelstatus', models.CharField(max_length=50)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.log')),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guidename', models.CharField(max_length=50)),
                ('guidephone', models.CharField(max_length=50)),
                ('guidemail', models.CharField(max_length=50)),
                ('guidelocation', models.CharField(max_length=50, null=True)),
                ('guidepincode', models.CharField(max_length=50, null=True)),
                ('guiderating', models.CharField(max_length=50, null=True)),
                ('Reviews', models.CharField(max_length=50, null=True)),
                ('guiderepass', models.CharField(max_length=50)),
                ('guidedp', models.ImageField(null=True, upload_to='images/')),
                ('role', models.CharField(max_length=50)),
                ('Guidesstatus', models.CharField(max_length=50)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.log')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Commenttext', models.CharField(max_length=50)),
                ('Createddate', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('spotname', models.CharField(max_length=50)),
                ('Commentsstatus', models.CharField(max_length=50)),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.spots')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.user')),
            ],
        ),
    ]
