from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth.models import User

from .models import UserEducation, Education, Major 
# from .models import UserEducation, Education, EducationMajor, Major 

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = (
            'id',
            'name',

            #general fields
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'id',
            'name',
            'logo',

            # general fields
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )    

class UserEducationSerializer(serializers.ModelSerializer):
    created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)

    class Meta:
        model = UserEducation
        fields = (
            'id',
            'education',
            'major',
            'degree',
            'begining_year',
            'end_year',
            
            # general fields
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )   
