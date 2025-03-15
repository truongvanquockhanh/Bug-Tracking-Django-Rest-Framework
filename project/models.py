from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=255, blank=True, default="Project", unique=True)
    description = models.CharField(max_length=512, blank=True)
    status = models.CharField(
       max_length=50, 
       default="open", 
       choices=(
          ('open', 'Open'),
          ('close', 'Close'),
       ),
    )
    priority = models.CharField(
       max_length=50, 
       default="low", 
       choices=(
          ('low', 'Low'),
          ('medium', 'Medium'),
          ('high', 'High'),
       ),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name="member_of_project", blank= True)

    class Meta:
      db_table = 'project'
      verbose_name = "Project"
      ordering = ("-created_at",)

