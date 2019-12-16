from django.shortcuts import render
from helper import parse_req_body
from app_user.models import *


# Create your views here.

def profile(request, pk):
    if request.method == 'POST':
        body = parse_req_body(request.body)
        pk = int(body['user_id'])
        if body['action'] == "Connect":
            profile_user = User.objects.get(pk=pk)
            if request.user.is_student and profile_user.is_mentor:
                Connection.objects.create(student=request.user, mentor=profile_user, request_from="S",status="P")
            elif request.user.is_mentor and profile_user.is_student:
                Connection.objects.create(student=profile_user, mentor=request.user, request_from="M",status="P")

    profile_user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=profile_user)
    
    if request.user.is_authenticated:
        if profile_user.is_student and request.user.is_mentor:
            profile_connection = Connection.objects.filter(student=profile_user).filter(mentor=request.user)
        elif profile_user.is_mentor and request.user.is_student:
            profile_connection = Connection.objects.filter(mentor=profile_user).filter(student=request.user)       
        else:
            profile_connection = None
    else:
        profile_connection = None

    context = { 
        'profile': profile,
        'profile_user': profile_user,
        'profile_connection':profile_connection,
        'pk': pk,
    }
    return render(request, 'profile/profile.html', context=context)        

def edit(request):
    user = request.user
    if request.method == 'POST':
        profile = Profile.objects.get(user=user)
        body = parse_req_body(request.body)
        uploaded_files = request.FILES
        if 'submit' in body:
            for variable in body:
                if body[variable] != "":
                    content = body[variable]
                    if variable == "new_first_name":
                        user.first_name = content
                    elif variable == "new_last_name":
                        user.last_name = content 
                    elif variable == "new_email":
                        user.email = content 
                    elif variable == "new_website":
                        profile.website = content                    
                    elif variable == "new_bio":
                        profile.bio = content
                    elif variable == "new_school":
                        new_school = School.objects.create(name=content)
                        user.schools.add(new_school)
                    elif variable == "new_major":
                        new_major = Major.objects.create(name=content)
                        user.majors.add(new_major)
                    elif variable == "new_industry":
                        new_industry = Industry.objects.create(name=content)
                        user.industries.add(new_industry)   
                    elif variable == "new_company":
                        new_company = Company.objects.create(name=content)
                        user.companies.add(new_company)      
        else:
            if 'delete_company' in body:
                company_id = body['company_id']
                company = Company.objects.get(pk=company_id)
                user.companies.remove(company)
                company.delete()

            elif 'delete_industry' in body:
                industry_id = body['industry_id']
                industry = Industry.objects.get(pk=industry_id)
                user.industries.remove(industry)
                industry.delete()            
            if 'delete_school' in body:
                school_id = body['school_id']
                school = School.objects.get(pk=school_id)
                user.schools.remove(school)
                school.delete()
            if 'delete_major' in body:
                major_id = body['major_id']
                major = Major.objects.get(pk=major_id)
                user.majors.remove(major)
                major.delete()


        user.save()
        profile.save() 
        # elif body['delete_industry']                  
                


    profile = Profile.objects.get(user=user)
    context = { 
        'profile': profile,
    }
    return render(request, 'profile/edit.html', context=context)        

