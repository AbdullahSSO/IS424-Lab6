from django.db import models

# Create your models here.


class course(models.Model):
    CID = models.CharField(max_length = 20,primary_key = True)
    InstructorName = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.CID}"


class student(models.Model):
    SID = models.CharField(max_length = 9,primary_key=True)
    FirstName = models.CharField(max_length = 64)
    LastName = models.CharField(max_length = 64)
    SPhoneNumber = models.CharField(max_length=10 )
    coures = models.ManyToManyField(course , blank=True,related_name = "students")


    def __str__(self):
        return f"{self.FirstName} {self.LastName}, {self.SID} "

