# Generated by Django 2.0 on 2017-12-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickettracker', '0002_auto_20171223_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='ticket',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='tickettracker.Tag', verbose_name='Tags'),
        ),
    ]
