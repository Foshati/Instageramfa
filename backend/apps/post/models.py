from django.db import models
from apps.user.models import User


def upload_to(instance, filename):
    return f"post/{instance.id}/{filename}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to=upload_to, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name="likes_set", blank=True, verbose_name="likes"
    )

    def __str__(self):
        return f"{self.author.username} - {self.id}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
