# Generated by Django 2.1.5 on 2019-01-09 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=256)),
                ('year', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('checked-out', 'Checked-Out')], default='available', max_length=128)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_borrowed', models.DateField()),
            ],
        ),
    ]