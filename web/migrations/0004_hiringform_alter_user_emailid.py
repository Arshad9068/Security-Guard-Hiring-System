# Generated by Django 4.1.7 on 2023-05-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_email_user_emailid'),
    ]

    operations = [
        migrations.CreateModel(
            name='hiringForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=50)),
                ('Shift', models.CharField(max_length=50)),
                ('ContactNo', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('NumberOfGuard', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='emailid',
            field=models.EmailField(default='', max_length=30),
        ),
    ]