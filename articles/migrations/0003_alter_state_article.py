# Generated by Django 3.2.13 on 2022-07-14 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220714_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='articles.article', verbose_name='статья'),
        ),
    ]