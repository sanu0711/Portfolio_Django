from django.contrib import admin
from onlinequiz.models import Student, Question, Result, Option, StudentSubmission
# Register your models here.
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Option)
admin.site.register(StudentSubmission)



