# Generated by Django 4.2.2 on 2023-06-26 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='house_id',
            new_name='house',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='task_id',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='house',
            name='members',
            field=models.ManyToManyField(to='schedule.user'),
        ),
        migrations.AddField(
            model_name='task',
            name='house',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='schedule.house'),
        ),
        migrations.AddField(
            model_name='user',
            name='houses',
            field=models.ManyToManyField(to='schedule.house'),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('user', 'house', 'task')},
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('task_name', 'house')},
        ),
        migrations.DeleteModel(
            name='House_composition',
        ),
    ]
