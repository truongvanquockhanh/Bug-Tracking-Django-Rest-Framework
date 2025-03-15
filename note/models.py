from django.db import models
from bugs.models import Bugs


class Note(models.Model):
    description = models.CharField(max_length=512, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    bugs = models.ManyToManyField(Bugs, related_name="Note_of_bugs", blank= True, null=True)

    class Meta:
      db_table = 'note'
      verbose_name = "Note"
      ordering = ("-created_at",)

