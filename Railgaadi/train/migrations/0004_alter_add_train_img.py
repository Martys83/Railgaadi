# Generated by Django 3.2.8 on 2021-11-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0003_auto_20211110_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_train',
            name='img',
            field=models.FileField(default='default.jpg', upload_to='train.pics'),
        ),
    ]
