from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    class Meta:
        db_table = 'skill'

    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='skill_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='skill_updated_by'
    )

class UserSkill(models.Model):
    class Meta:
        db_table = 'user_skill'

    skill = models.ForeignKey(
        Skill,
        on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_skill_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_skill_updated_by'
    )
