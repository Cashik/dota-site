from dis import _format_code_info

from django.db import models
from django.utils import timezone
from django.conf import settings
import random
import string

def make_upload_path(asd, filename):
    new_file_name = ''
    for i in range(16):
        new_file_name+=random.choice(string.ascii_letters)
    new_file_name += "_"+str(timezone.now().date())
    return (u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, new_file_name))

class News(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        verbose_name="Изображение")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title