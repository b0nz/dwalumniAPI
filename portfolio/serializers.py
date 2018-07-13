from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    skill = RecursiveField('skill.serializers.SkillSerializerSimple', read_only=True)

    created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)

    class Meta:
        model = Portfolio
        fields = (
            'id',
            'title',
            'description',
            'github_url',
            'skill',

            # general fields
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )
