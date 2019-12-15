from django.shortcuts import render
from django.db.models import Q
from app_user.models import User

def searchusers(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(first_name__icontains=query) | Q(last_name__icontains=query) |Q(position__icontains=query) | Q(companies__name__icontains=query) | Q(requests__name__icontains=query)|Q(schools__name__icontains=query)|Q(majors__name__icontains=query)|Q(industries__name__icontains=query)
            results= User.objects.filter(lookups).distinct()

            context={
                     'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search/search.html', context)

        else:
            return render(request, 'search/search.html')

    else:
        return render(request, 'search/search.html')