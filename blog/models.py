from django.db import models
#from django.utils import timezone


class Post(models.Model):
    captial= models.IntegerField(default=0, blank=True, null=True)
    year= models.IntegerField(default=0, blank=True, null=True)
    rate= models.IntegerField(default=0, blank=True, null=True)

    #created_date = models.DateTimeField(
     #       default=timezone.now)
    #published_date = models.DateTimeField(
     #       blank=True, null=True)

    #def publish(self):
     #   self.published_date = timezone.now()
       # self.save()

    #def __str__(self):
     #   return self.title

#@savings 
#def calculate_savings(savings):
    #return (a = p * [ 1+[[r/100]/12]]^[12*y])

  
