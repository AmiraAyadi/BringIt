from django.shortcuts import render
from django.core import serializers

import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from custom_user.models import AbstractEmailUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_modal(request):
    return render(request, 'login.html',{})

def login(request):
    response_data = {'status' : 'failure', 'message' : 'an unknown error occured'}
    if request.is_ajax():
        if request.method == 'POST':
            user = authenticate(
                email=request.POST.get('email').lower(),
                password=request.POST.get('mdp')
            )
            
            # Does the user exist for the username and has correct password?
            if user is not None:
                # Is user suspended or active?
                if user.is_active:
                    response_data = {'status' : 'success', 'message' : 'logged on'}
                    login(request, user)
                else:
                    response_data = {'status' : 'failure', 'message' : 'you are suspended'}
            else:
                response_data = {'status' : 'failure', 'message' : 'wrong username or password'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")