# Generated by Django 2.0.2 on 2018-06-26 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detail_skill_created_by', to=settings.AUTH_USER_MODEL)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill.Skill')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detail_skill_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'detail_skill',
            },
        ),
        migrations.CreateModel(
            name='UserDetailSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detail_user_skill_created_by', to=settings.AUTH_USER_MODEL)),
                ('skill_exam_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail_skill.DetailSkill')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detail_user_skill_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'detail_user_skill',
            },
        ),
    ]
