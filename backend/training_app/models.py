from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

class Training(models.Model):
    date = models.DateTimeField('Training Date')
    training_menu = models.CharField(max_length=200)
    training_memo = models.TextField()