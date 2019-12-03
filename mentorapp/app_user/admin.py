from django.contrib import admin

# Register your models here.
from .models import User, Request, School, Company, Industry, Major, Student, Mentor

admin.site.register(User)
admin.site.register(Request)
admin.site.register(School)
admin.site.register(Major)
admin.site.register(Company)
admin.site.register(Industry)
admin.site.register(Student)
admin.site.register(Mentor)

