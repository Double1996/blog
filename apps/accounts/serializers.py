from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

from .models import Token

"""
    fork from django-rest-auth 'https://github.com/Tivix/django-rest-auth/blob/master/rest_auth/serializers.py'
"""
# 获取用户模型
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'username',
            'email',

        ]

    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError("用户已被注册")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.is_active = False
        user_obj.save()
        return validated_data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = authenticate(email=email, password=password)
        else:
            msg = '必须输入电子邮件或者密码.'
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = '必须输入用户名或者密码.'
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username_email(self, username, email, password):
        user = None

        if email and password:
            user = authenticate(email=email, password=password)
        elif username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = '必须输入正确的用户名或者是正确的电子邮箱'
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = None

        if email:
            try:
                username = User.objects.get(email__iexact=email).get_username()
            except User.DoesNotExist:
                pass

        if username:
            user = self._validate_username(username=username, password=password)

        if user:
            if not user.is_active:
                msg = '您的账号还没被激活!'
                raise exceptions.ValidationError(msg)
        else:
            msg = '账号验证未通过'
            raise exceptions.ValidationError(msg)
        attrs['user'] = user
        return attrs


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = Token
        fields = ('key',)


class UserDetailSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('email',)
