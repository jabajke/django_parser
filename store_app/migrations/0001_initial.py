# Generated by Django 3.2.9 on 2021-11-25 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parse_app', '0011_alter_parsedata_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('item_total', models.DecimalField(decimal_places=0, max_digits=9)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parse_app.parsedata')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_total', models.DecimalField(decimal_places=0, max_digits=9)),
                ('items', models.ManyToManyField(blank=True, to='store_app.CartModel')),
            ],
        ),
    ]