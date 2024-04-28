from django.db import models


class NameMixin(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PostbleMixin(TimeStampMixin):
    content = models.TextField()
    likes = models.IntegerField(default=0)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True
