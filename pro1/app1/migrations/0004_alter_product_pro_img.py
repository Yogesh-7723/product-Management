# Generated by Django 4.2.3 on 2023-12-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_product_pro_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_img',
            field=models.FileField(blank=True, upload_to='upload/'),
        ),
    ]