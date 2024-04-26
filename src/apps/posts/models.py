from django.db import models
from apps.entities.models import Profile
from utils.mixins import NameMixin, PostbleMixin


class Tag(NameMixin):
    ...


class Post(PostbleMixin):
    title = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT
    )
    tags = models.ManyToManyField(Tag)


class Comment(PostbleMixin):
    parent_id = models.IntegerField(
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT
    )
