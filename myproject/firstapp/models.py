from django.db import models

# Create your models here.
class Cards(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    readtime = models.IntegerField(default=0)

#model Inheritance
class BasicInfo(models.Model):
    GENDER = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    name = models.CharField(max_length=100)
    gender =models.CharField(choices=GENDER)
    email = models.EmailField()
    address =models.TextField()
    mobile =models.IntegerField()
    
    class Meta:
        abstract = True

class Teacher(BasicInfo):
    qualification = models.CharField(max_length=50)
    hired_date = models.DateField()

class Student(BasicInfo):
    def __str__(self):
        return self.name
    
    
# one to many relationship
# A student can have multiple courses, but a course can only have one student.
class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fee = models.IntegerField()
    def __str__(self):
        return self.name

# one to one relationship

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bio = models.TextField()

#many to many relationship

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name   

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')
    def __str__(self):
        return self.title
    