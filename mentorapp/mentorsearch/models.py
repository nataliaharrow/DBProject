from django.db import models

# Create your models here.

# classes represent tablers in our database
# and field names are DB column names

from django.db import models

# UserTypes (userTypeId, userTypeName) (Types: Students, Mentors)
class UserType(models.Model):
    user_type_name = models.CharField(max_length=10)

# Users (userId, firstName, lastName, emailAddress, userTypeId)
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000, default='bio')
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

# Schools (schoolId, schoolName, schoolAddress, schoolType)
class School(models.Model):
    school_name = models.CharField(max_length=30)
    school_address = models.CharField(max_length=200)

# Industries (industryId, industryName)
class Industry(models.Model):
    industry_name = models.CharField(max_length=30)

# Companies (companyId, industryId, companyName, companyAddress)
class Company(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    company_address = models.CharField(max_length=200)

# Mentors (userId, schoolId, industryId, position)
class Mentor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=40)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

# Majors (majorId, majorName)
class Major(models.Model):
    major_name = models.CharField(max_length=30)

# Students (userId, schoolId, majorId)
class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

# Requests (requestId, requestType) (Types: e.g. Resume, Interview, Network, etc)
class Request(models.Model):
    request_type = models.CharField(max_length=30)

# Missing tables:
# Profiles (userId, userPhoto)
# Connections (userId, connectionId, timeStamp)
# StudentIndustryInterests (userId, industryId) (Relation: Student has m IndustryInterests)
# StudentRequests (userId, requestId, industryId, connectionId) (Relation: Student asks m Requests)
# Profiles (userId, userPhoto)
# Messages (userId, connectionId, messageContent, timeStamp)
# MentorsCompanies(userId, companyId, jobTitle) (Relation: Mentors worked in m Companies)