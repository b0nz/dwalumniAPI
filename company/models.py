from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    class Meta:
        db_table = "company"

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='company_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='company_updated_by'
    )

def __str__(self):
    return self.name
