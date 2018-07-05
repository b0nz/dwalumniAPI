# Generated by Django 2.0.2 on 2018-07-04 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationmajor',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='educationmajor',
            name='education',
        ),
        migrations.RemoveField(
            model_name='educationmajor',
            name='major',
        ),
        migrations.RemoveField(
            model_name='educationmajor',
            name='updated_by',
        ),
        migrations.RenameField(
            model_name='usereducation',
            old_name='degeree',
            new_name='degree',
        ),
        migrations.AddField(
            model_name='usereducation',
            name='major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Major'),
        ),
        migrations.DeleteModel(
            name='EducationMajor',
        ),
    ]