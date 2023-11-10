from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.name} {self.user} {self.score}'
   
class Question(models.Model):
    Q= models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.Q
class StudentSubmission(models.Model):
    user = models.CharField(max_length=100)
    questionNo = models.CharField(max_length=100)
    submittime = models.DateTimeField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user} {self.questionNo} {self.submittime} {self.status}'


class Result(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.user

class Option(models.Model):
    user = models.CharField(max_length=100)
    option = models.CharField(max_length=100)
    def __str__(self):
        return self.option




