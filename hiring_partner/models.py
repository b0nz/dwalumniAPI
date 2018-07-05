from django.db import models
from django.contrib.auth.models import User
from company.models import Company

class HiringPartner(models.Model):
    class Meta:
        db_table = "hiring_partner"

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hiring_partner_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hiring_partner_updated_by'
    )
