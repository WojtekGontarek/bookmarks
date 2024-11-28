from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    url = models.URLField(max_length=250)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(User, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.title))
        super().save(*args, **kwargs)

