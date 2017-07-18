from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	response = "Hello, This is blogs"
	return HttpResponse(response)

def new(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)

def create(request):
	return redirect(index)

def show(request,number):
	print number
	return HttpResponse('placeholder to display blog '+number)

def edit(request,number):
	print number
	response = "placeholder to edit blog "+number
	return HttpResponse(response)

def destroy(request,number):
	response =  "Have this be handled by a method named 'destroy'. For now, have this url redirect to /blogs."
	return redirect(index) 