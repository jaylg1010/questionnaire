from django.contrib import admin
from app01 import models

# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.ClassList)
admin.site.register(models.Student)
admin.site.register(models.Questionnaire)
admin.site.register(models.Question)
admin.site.register(models.Option)
admin.site.register(models.Answer)