from rest_framework import serializers
from .models import Tag, Category, Comment, Post


class PostCreateSerializer(serializers.ModelSerializer):
    pass


class PostDeatailSerializer(serializers.ModelSerializer):
    pass


class PostListSerialzier(serializers.ModelSerializer):
    pass
