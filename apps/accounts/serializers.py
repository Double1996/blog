from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions

"""
    fork from django-rest-auth 'https://github.com/Tivix/django-rest-auth/blob/master/rest_auth/serializers.py'
"""
# 获取用户模型
UserModel = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, all_blank=True)
    email = serializers.CharField(required=True, all_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = authenticate(email=email, password=password)
        else:
            msg = _('必须输入电子邮件或者密码.')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = _('必须输入用户名或者密码.')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username_email(self, username, email, password):
        user = None

        if email and password:
            user = authenticate(email=email, password=password)
        elif username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = _('必须输入正确的用户名或者是正确的电子邮箱')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = None

        if email:
            try:
                username = UserModel.objects.get(email__iexact=email).get_username()
            except UserModel.DoesNotExist:
                pass

        if username:
            user = self._validate_user_name(username=username, password=password)

        if user:
            if not user.is_active:
                msg = _('您的账号还没被激活!')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('账号验证未通过')
            raise exceptions.ValidationError(msg)
        attrs['user'] = user
        return attrs

