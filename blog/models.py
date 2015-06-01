from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):

    author=models.ForeignKey('auth.user')
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def publish(self):
        
        self.published_date=timezone.now()
        self.save()


    def __unicode__(self): #use __str__ in case of python3
        return self.title