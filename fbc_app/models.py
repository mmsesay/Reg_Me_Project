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
    requirements = models.TextField()
    university = models.ForeignKey(University, related_name="courses", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# module class
class Module(models.Model):
    module_code = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    credit_hours = models.CharField(max_length=50)
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# lecturer class
class Lecturer(models.Model):
    name = models.CharField(max_length=256)
    address = models.TextField()
    university = models.ForeignKey(University, related_name="lecturers", on_delete=models.CASCADE)
    module = models.ForeignKey(Module, related_name="lecturers", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# student class
class Student(models.Model):
    name = models.CharField(max_length=256)
    email =  models.EmailField(blank=True)
    address = models.TextField(blank=True)
    age = models.PositiveIntegerField()
    university = models.ForeignKey(University, related_name='students', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='students', on_delete=models.CASCADE)
    module = models.ForeignKey(Module, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
