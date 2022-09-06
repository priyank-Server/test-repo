from django.db import models
from user.models import User
from apps.blog.models import Category, Tag
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from django.contrib.postgres.fields import ArrayField


class Snippet(TimeStampedModel, ActivatorModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippet', default=True)
    title = models.CharField(max_length=255)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='snippet', default=True)
    tag = models.ManyToManyField(Tag, related_name='snippet')
    slug = AutoSlugField(populate_from=['title'])
    allow_comments = models.BooleanField()
    version = ArrayField(models.CharField(max_length=255))

    class Meta:
        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'

    def __str__(self):
        return self.title
