from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User, Group
from rest_framework_recursive.fields import RecursiveField
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email','password',)

    def save(self):
        user = User.objects.create_user(
            self.validated_data['username'],
            self.validated_data['email'],
            self.validated_data['password']
        )
        user_group = Group.objects.get(id=1)
        user.groups.add(user_group)
        return user


class UserSerializerSimple(UserSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = RecursiveField('user.serializers.UserSerializer',read_only=True)

    created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)

    birthdate = serializers.DateTimeField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Profile
        fields = (
            'id',
            'birthdate',
            'user',
            'about',
            'address',
            'expectation_salary',
            'expectation_work_location',
            'hired_by',
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )
