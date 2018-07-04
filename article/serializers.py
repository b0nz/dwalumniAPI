from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Article
from user.serializers import UserSerializerSimple

class ArticleSerializer(serializers.ModelSerializer):
    created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    #user = UserSerializerSimple(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'body',
            'pic',
            'user',
            'skill',

            # general fields
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
            'is_active',
        )
    
