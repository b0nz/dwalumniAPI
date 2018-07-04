from django.db import models
from django.contrib.auth.models import User
from skill.models import Skill

class Article(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=128)
    body = models.TextField(blank=True, null=False)
    pic = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    skill = models.ForeignKey(
       Skill,
       on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='article_created_by'
    )
    updated_by = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='article_updated_by'
    )
