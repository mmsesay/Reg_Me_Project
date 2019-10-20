from django.db import models

# university class
class University(models.Model):
    name = models.CharField(max_length=256)
    chancellor = models.CharField(max_length=256)
    location =  models.CharField(max_length=256)

    def __str__(self):
        return self.name

# course class
class Course(models.Model):
    title = models.CharField(max_length=250)
    requirements = models.CharField()
    university = models.ForeignKey(University, related_name="courses")

    def __str__(self):
        return self.title



# student class
class Student(models.Model):
    name = models.CharField(max_length=256)
    email =  models.EmailField()
    address = models.CharField()
    age = models.PositiveIntegerField()
    university = models.ForeignKey(University, related_name='students')

    def __str__(self):
        return self.name

