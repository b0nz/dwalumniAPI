from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import DetailSkill, UserDetailSkill

class DetailSkillSerializer(serializers.ModelSerializer):
    created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)

    class Meta:
        model = DetailSkill
        fields = (
            'id',
            'name',
            'skill',

            # general fields
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )

class UserDetailSkillSerializer(serializers.ModelSerializer):
    created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)

    class Meta:
        model = UserDetailSkill
        fields = (
            'id',
            'detail_skill',
            'user',
            
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )
