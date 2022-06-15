# Generated by Django 3.0.8 on 2022-06-01 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sabiman', '0002_auto_20220527_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number_1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number_2',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Lecturer', 'Lecturer')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_department', to='sabiman.Department'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='role',
            field=models.CharField(choices=[('course adviser', 'course adviser'), ('HOD', 'HOD')], default='normal', max_length=16, null=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]