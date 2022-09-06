from rest_framework import serializers
from apps.snippet import models
from apps.blog.models import Tag, Category
from django.contrib.humanize.templatetags.humanize import naturaltime


class ReadTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'word']


class ReadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'word']


class SnippetSerializer(serializers.ModelSerializer):
    tag = ReadTagSerializer(read_only=True, many=True)
    category = ReadCategorySerializer(read_only=True, many=False)
    user = serializers.SerializerMethodField(read_only=True)
    day_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    def get_day_count(self, obj):
        return naturaltime(obj.created)

    class Meta:
        model = models.Snippet
        fields = ['id', 'user', 'title', 'description', 'slug', 'allow_comments', 'tag', 'category',  'version',
                  'tag', 'category', 'user', 'day_count']


class ReadTagSnippetSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = models.Snippet
        fields = ['id', 'created', 'modified', 'title', 'slug', 'user', 'category']


class ReadCategorySnippetSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(read_only=True, many=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = models.Snippet
        fields = ['id', 'created', 'modified', 'title', 'slug', 'user', 'tag']
