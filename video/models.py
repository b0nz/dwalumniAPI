from django.db import models
from django.contrib.auth.models import User
from skill.models import Skill

class Video(models.Model):
    class Meta:
        db_table = "video"

    title = models.CharField(max_length=128)
    video_url = models.CharField(max_length=255)
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
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='video_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='video_updated_by'
    )
