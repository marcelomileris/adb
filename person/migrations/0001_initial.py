# Generated by Django 3.2.5 on 2021-07-13 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('cpf', models.CharField(max_length=14)),
                ('phone', models.CharField(max_length=15)),
                ('company', models.CharField(max_length=32)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person_media_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Person_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Person_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person.person_media_type')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person.person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('cpf_new', models.CharField(max_length=14)),
                ('cpf_old', models.CharField(max_length=14)),
                ('last_update', models.DateTimeField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person.person_type')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person.person_type'),
        ),
    ]
