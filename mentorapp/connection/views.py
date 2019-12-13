from django.shortcuts import render
from app_user.models import *
from helper import parse_req_body

# Create your views here.
def connections(request):
    user = request.user
    if request.method == "POST":
        body = parse_req_body(request)
        if body['task'] == edit_connection:
            if body['action'] == 'Remove':
                connection_id = int(body['connection_id'])
                Connection.objects.delete(pk=connection_id)
            elif body['action'] == 'Approve':
                connection_id = int(body['connection_id'])
                connection = Connection.objects.get(pk=connection_id)
                connection.status = 'C'
            elif body['action'] == 'Connect':
                other_user_id = int(body['other_user_id'])
                other_user = User.objects.get(pk=other_user_id)
                if user.is_student:
                    connection = Connection(student=user, mentor=other_user, status='P', request_from='S')
                else:
                    connection=Connection(mentor=user, student=other_user, status='P', request_from='M')
        if user.is_student:
            connections = Connection.objects.filter(student=user)
        else:
            connections = Connection.objects.filter(mentor=user)
        context = {'connections': connections}
        return(request, 'connections.html', context)

    elif request.method == "GET":
        if user.is_student:
            connections = Connection.objects.filter(student=user)
        else:
            connections = Connection.objects.filter(mentor=user)
        context = {'connections': connections}
        return(request, 'connections.html', context)