from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from user.models import User
from django.contrib.postgres.fields import ArrayField
from ckeditor.fields import RichTextField


class Tag(models.Model):
    word = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['word'], null=True, blank=True)
    description = RichTextField()

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.word


class Category(models.Model):
    word = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['word'])
    description = RichTextField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.word


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'blog_{}/{}'.format(instance.slug, filename)


class Blog(TimeStampedModel, ActivatorModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Blogs', default=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Blogs')
    tag = models.ManyToManyField('Tag', related_name='Blogs')
    slug = AutoSlugField(populate_from=['title'])
    allow_comments = models.BooleanField()
    version = ArrayField(models.CharField(max_length=255))

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
