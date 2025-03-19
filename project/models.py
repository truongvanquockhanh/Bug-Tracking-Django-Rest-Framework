from django.db import models
from users.models import User

class Status(models.TextChoices):
    OPEN = 'open', 'Open'
    CLOSED = 'closed', 'Closed'

class Priority(models.TextChoices):
    LOW = 'low', 'Low'
    MEDIUM = 'medium', 'Medium'
    HIGH = 'high', 'High'

class Project(models.Model):
    name = models.CharField(max_length=255, blank=True, default="Project", unique=True)
    description = models.CharField(max_length=512, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.OPEN)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.LOW)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name="member_of_project", blank= True)
    owner_by = models.ForeignKey (
       User, on_delete=models.CASCADE, blank= True
    )

    class Meta:
      db_table = 'project'
      verbose_name = "Project"
      ordering = ("-created_at",)

