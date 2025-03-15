from django.db import models
from project.models import Project


class Bugs(models.Model):
    title = models.CharField(max_length=255, blank=True, default="Project")
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
    project = models.ManyToManyField(Project, related_name="Bugs_of_project", blank= True)

    class Meta:
      db_table = 'bugs'
      verbose_name = "Bugs"
      ordering = ("-created_at",)

