from django.db import models
from django.contrib.auth.models import User
from skill.models import Skill

class DetailSkill(models.Model):
    class Meta:
        db_table = "detail_skill"

    name = models.CharField(max_length=50)
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='detail_skill_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='detail_skill_updated_by'
    )

def __str__(self):
    return self.name

class UserDetailSkill(models.Model):
    class Meta:
        db_table = "detail_user_skill"

    detail_skill = models.ForeignKey(
        DetailSkill,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='detail_user_skill_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='detail_user_skill_updated_by'
    )
