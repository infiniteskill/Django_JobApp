from django.db import models
from django.utils.timezone import now

# Create your models here.
class Job(models.Model):
    position=models.CharField(max_length=200)
    experience=models.CharField(max_length=10)
    location=models.CharField(max_length=200)

    
    company=models.CharField(max_length=200)
    skills=models.CharField(max_length=500)
    contact=models.CharField(max_length=500)
    postdate=models.DateField(default=now,editable=False)
    
    

    def __str__(self):
        job_detail= self.position ,self.location,self.company,self.experience+" year",self.postdate
        return str(job_detail)


