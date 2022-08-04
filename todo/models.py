from django.db import models

# Create your models here.

class task(models.Model):
    task_text=models.CharField(max_length=500,default="task")

    def __str__(self):
        return self.task_text

    def save(self):
        super(task,self).save()