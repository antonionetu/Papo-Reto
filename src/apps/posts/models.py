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

    class Meta:
        abstract = True


class Author(TimeStampMixin, NameMixin):
    born_date = models.DateField()


class Post(PostbleMixin):
    title = models.CharField(max_length=255)
    viewers_count = models.IntegerField(default=0)
    author = models.ForeignKey(
        Author,
        related_name='posts',
        on_delete=models.PROTECT
    )


class Tag(NameMixin):
    ...


class Comment(PostbleMixin):
    parent_id = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='comments',
        on_delete=models.PROTECT
    )
