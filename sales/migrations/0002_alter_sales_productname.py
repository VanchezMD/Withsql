# Generated by Django 4.1.1 on 2022-09-28 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='productName',
            field=models.ForeignKey(db_column='product', on_delete=django.db.models.deletion.CASCADE, to='sales.products'),
        ),
    ]