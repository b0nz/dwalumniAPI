from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth.models import User

from .models import UserEducation, Education, Major 
# from .models import UserEducation, Education, EducationMajor, Major 

class MajorSerializer(serializers.ModelSerializer):
    # created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    # updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    # education_major = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='id'
    # )

    class Meta:
        model = Major
        fields = (
            'id',
            'name',
            # 'education_major',

            #general fields
            'is_active',
            # 'created_at',
            # 'updated_at',
            # 'created_by',
            # 'updated_by',
        )

class EducationSerializer(serializers.ModelSerializer):
    # created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    # updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)

    class Meta:
        model = Education
        fields = (
            'id',
            'name',
            'logo',

            # general fields
            'is_active',
            # 'created_at',
            # 'updated_at',
            # 'created_by',
            # 'updated_by',
        )    

# class EducationMajorSerializer(serializers.ModelSerializer):
#     # created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
#     # updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
#     major = MajorSerializer()
#     education = EducationSerializer()

#     class Meta:
#         model = EducationMajor
#         fields = (
#             'id',
#             'major',
#             'education',
            
#             # general fields
#             'is_active',
#             'created_at',
#             'updated_at',
#             'created_by',
#             'updated_by',
#         )
    
#     def create(self, validated_data):
#         created_by_id = validated_data.get("created_by_id")
#         validated_data.pop("created_by_id", None)
        
#         education_major = Courses(**validated_data)

#         # relate with user
#         user = User.objects.filter(id=created_by_id).first()
#         education_major.created_by = user
#         education_major.save()

#         return education_major

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
            'user',
            
            # general fields
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )   
