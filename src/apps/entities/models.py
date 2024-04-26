from django.db import models
from utils.mixins import NameMixin, TimeStampMixin


class Profile(NameMixin, TimeStampMixin):
    is_unit_student = models.BooleanField(default=False)
