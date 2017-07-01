from django.shortcuts import render
from django.utils import timezone
from .models import Post ,box

from django.shortcuts import render

from django.http import HttpResponse
#from .models import Weather

from django.http import JsonResponse
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import sys
from django.contrib.auth.forms import PasswordChangeForm

from flask_socketio import SocketIO, send, emit 
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myapp/post_list.html', {'posts': posts})
def control(request):
	return render(request,'smb/admin.html')
def smb(request):
	return render(request,'smb/smb.html')
def home(request):
	return render(request,'home.html')
def signin(request):
	if request.method == 'POST' and 'username' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print >>sys.stderr, "debug"
		if user is not None:
			if user.is_active:

				if 'remember' in request.POST:
					print>>sys.stderr, "%s type: %s"%(request.POST['remember'],type(request.POST['remember']))
					if request.POST['remember']=='1':
						request.session.set_expiry(604800) #remember keep session for a week
				else:
					request.session.set_expiry(14400) #not remember keep session for 4hrs
				print >>sys.stderr, "session expiry: %s"%request.session.get_expiry_age()

				login(request, user)
				if 'username' in request.session:
					print >>sys.stderr, "username_i: %s"%request.session['username']
				request.session['username'] = user.username
				print >>sys.stderr, "username_f: %s"%request.session['username']
				
				return redirect('home')
			else:
				msg="Disabled account"
		else:
			msg="Invalid username or password"
		return render(request,'login.html',{'msg': msg})   
	return render(request,'login.html',{'msg': ""})

def signout(request):
	print "signout"
	if 'username' in request.session:
		del request.session['username']
		print "del uname"
	logout(request)
	return redirect('smb')

#@login_required(login_url='signin')

def change_password(request):
    form = PasswordChangeForm(user=request.user)
    print >>sys.stderr, "request.user: %s"%request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('class_page')

    return render(request, 'change_password.html', {
        'form': form,
    })

def getdata(request):
	data_box = box(
	nodeid = request.GET['nodeid'],
	temp 	= float(request.GET['temp']), 
	humi 	= float(request.GET['humi']),
		)
	data_box.save()
	return HttpResponse("Command",content_type='text/plain')