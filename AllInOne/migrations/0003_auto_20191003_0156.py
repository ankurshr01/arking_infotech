# Generated by Django 2.2.5 on 2019-10-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllInOne', '0002_auto_20190929_0758'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
