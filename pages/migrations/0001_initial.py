# Generated by Django 4.2.6 on 2023-11-14 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('livro', models.CharField(max_length=200)),
                ('autor_livro', models.CharField(max_length=200)),
                ('data', models.DateTimeField()),
                ('conteudo', models.TextField()),
            ],
        ),
    ]
