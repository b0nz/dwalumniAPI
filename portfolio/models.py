from django.db import models
from django.contrib.auth.models import User
from skill.models import Skill

class Portfolio(models.Model):
    class Meta:
        db_table = 'portfolio'

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=False)
    github_url = models.CharField(max_length=255)
    skill    = models.ForeignKey(
        Skill,
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
        related_name='portfolio_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='portfolio_updated_by'
    )

def __str__(self):
    return self.title
