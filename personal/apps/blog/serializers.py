from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework.response import Response

from apps.blog.models import Tag, Category, Blog
from apps.snippet.serializers import ReadTagSnippetSerializer, ReadCategorySnippetSerializer
from user.models import User
from rest_framework_simplejwt.serializers import TokenObtainSerializer


class ReadTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['word']


class ReadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['word']


class ReadBlogSerializer(serializers.ModelSerializer):
    tag = ReadTagSerializer(read_only=True, many=True)
    category = ReadCategorySerializer(read_only=True, many=False)
    user = serializers.StringRelatedField()
    day_count = serializers.SerializerMethodField()

    def get_day_count(self, obj):
        return naturaltime(obj.created)

    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'image', 'description', 'slug', 'allow_comments', 'category', 'tag', 'version',
                  'user', 'day_count']


class ReadCategoryBlogSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(read_only=True, many=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = ['id', 'created', 'modified', 'title', 'image', 'slug', 'user', 'tag']


class ReadTagBlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = ['id', 'created', 'modified', 'title', 'image', 'slug', 'user', 'category']


class TagSerializer(serializers.ModelSerializer):
    Blogs = ReadTagBlogSerializer(read_only=True, many=True)
    snippet = ReadTagSnippetSerializer(read_only=True, many=True)

    class Meta:
        model = Tag
        fields = ['id', 'word', 'slug', 'Blogs', 'snippet']


class CategorySerializer(serializers.ModelSerializer):
    Blogs = ReadCategoryBlogSerializer(read_only=True, many=True)
    snippet = ReadCategorySnippetSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['id', 'word', 'slug', 'Blogs', 'snippet']
