# Generated by Django 3.1.7 on 2021-02-19 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateField()),
                ('code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField()),
                ('price', models.CharField(max_length=10)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.ticket')),
            ],
        ),
    ]