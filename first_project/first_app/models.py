from django.db import models

# Create your models here.
class Topic(models.Model):
    """docstring forTopic."""
    top_name= models.CharField(max_length=264,unique=True)

    def __str__(self):
        return  self.top_name

class Webpage(models.Model):
    topic=models.ForeignKey(Topic)
    name=models.CharField(max_length=264, unique=True)
    url=models.UrlField(unique=True)

    def __str__(self):
        return  self.name

class AccessDate(models.Model):
    name=models.ForeignKey(Webpage)
    date =models.DateField()

    def __str__(self):
        return  str(self.date)
                
