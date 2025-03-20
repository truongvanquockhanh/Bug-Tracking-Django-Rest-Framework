from django.db import models
from project.models import Project


class Status(models.TextChoices):
    OPEN = 'open', 'Open'
    CLOSED = 'closed', 'Closed'


class Priority(models.TextChoices):
    LOW = 'low', 'Low'
    MEDIUM = 'medium', 'Medium'
    HIGH = 'high', 'High'


class Bugs(models.Model):
    title = models.CharField(max_length=255, blank=True, default="Project")
    description = models.CharField(max_length=512, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.OPEN)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.LOW)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ManyToManyField(Project, related_name="bugs", blank=True)

    class Meta:

      db_table = 'bugs'
      verbose_name = "Bugs"
      ordering = ("-created_at",)
