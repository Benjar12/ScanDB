from django.shortcuts import render
import os
import sys
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from OCR.models import DocUpload
from OCR.forms import DocUploadForm, UserForm, UserProfileForm
CV_CODE_PATH=settings.BASE_DIR+'/CVCode/'
sys.path.insert(0, CV_CODE_PATH)
import GetData

def index(request):
    #print os.listdir(settings.BASE_DIR)
    #print settings.BASE_DIR
    if request.method == 'POST':
        form = DocUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = DocUpload(uploaded_doc = request.FILES['uploaded_doc'])
            newdoc.save()
            IMAGE_PATH=str(newdoc)
            GetData.start(IMAGE_PATH)
            return render(request, 'OCR/user.html', {'url':str(newdoc)})
        else:
            print form.errors
            return HttpResponse('image upload failed')
    else:
        form=DocUploadForm()

    context_dict = {'boldmessage': "ResearchUSA", 'form':form}
    return render(request, 'OCR/index.html', context_dict)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/OCR/user/')
            else:
                return HttpResponse("Your ResearchUSA account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'OCR/login.html', {})
    

def user(request):
    return render(request, 'OCR/user.html', {})

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
            'OCR/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )