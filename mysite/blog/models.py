from django.db import models
from datetime import datetime

# Create your models here.


class Blog(models.Model):

    title = models.CharField(max_length=50)

    body = models.TextField()

    pub_date = models.DateTimeField('date published')


    # def __str__(self):
    #     return self.body[:100]