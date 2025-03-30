from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    periority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.title} => is Done:{self.is_done}'
    
    class Meta:
        db_table = "todos"