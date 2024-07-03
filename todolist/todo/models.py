from django.db import models


class Tod(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    completed=models.BooleanField(default=False)

    def __str__(self) ->str:
        return self.title
# Create your models here.
