from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "tags"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.content
