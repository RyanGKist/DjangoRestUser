from django.shortcuts import render, HttpResponse, redirect

from models import *


def index(request):
	return render(request, 'restApp/index.html', {"User": User.objects.all() })

def create(request):
	return render(request, 'restApp/create.html')

def user_create(request):
	errors = User.objects.basic_validation(request.POST)
	if len(errors):
		for tag , error in errors.iteritems():
			messages.error(request,error,extra_tags=tag)
			return redirect('/')
	else:
		User.objects.create(name=request.POST['name'] , email=request.POST['email'])
		return redirect('/')

def edit_collect(request, uid):
	
	context = {
	'User': User.objects.get(id=uid) 
	}
	print uid
	print context
	return render(request,'restApp/edit.html',context)

def edit_user(request,uid):

	errors = User.objects.basic_validation(request.POST)
	if len(errors):
		for tag , error in errors.iteritems():
			messages.error(request,error,extra_tags=tag)
			return redirect('/')
	else:
		c = User.objects.get(id=uid)
		c.name = request.POST['name']
		c.email= request.POST['email']
		c.save()
		return redirect ('/')

def delete(request,uid):
	User.objects.get(id=uid).delete()
	return redirect('/')

def show(request,uid):
	return render(request, 'restApp/show.html', {"User": User.objects.get(id=uid) })

