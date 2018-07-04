from django.db import models
from django.contrib.auth.models import User
    

class Profile(models.Model):
    class Meta:
        db_table = "profile"

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True, default='no_image.jpg')
    birthdate = models.DateField()
    about = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    expectation_salary = models.FloatField()
    expectation_work_location = models.CharField(max_length=255)
    
    user = models.ForeignKey(
        User,
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
        related_name='profile_created_by'
    )
    updated_by = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profile_updated_by'
    )