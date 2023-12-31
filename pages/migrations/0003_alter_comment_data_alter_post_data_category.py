# Generated by Django 4.2.6 on 2023-11-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_post_data_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='data',
            field=models.DateTimeField(default='2023-11-20 14:37:23'),
        ),
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateTimeField(default='2023-11-20 14:37:23'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('posts', models.ManyToManyField(to='pages.post')),
            ],
        ),
    ]
