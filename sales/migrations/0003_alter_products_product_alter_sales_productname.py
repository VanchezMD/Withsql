# Generated by Django 4.1.1 on 2022-09-28 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sales_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='productName',
            field=models.ForeignKey(db_column='product', on_delete=django.db.models.deletion.CASCADE, to='sales.products', to_field='product'),
        ),
    ]
