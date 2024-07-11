from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.



def AdminLogin(request):
	if request.method=='POST': 
		name=request.POST.get('username')
		pwd=request.POST.get('password')
		try:
			user=authenticate(request,username=name,password=pwd)
			if user is not None:
				admin=User.objects.filter(id=user.id).first()
				if admin.is_superuser==1:
					login(request,user)
					print("login")
					return redirect('home')
				else:
					messages.error(request,'Username or Password Does not match')
					return redirect('login')  
                	
		except:
			messages.error(request,'Username or Password Does not match')
			return redirect('login')

	else:
		return render(request,'login.html')


def Home(request):
	users=UserDetails.objects.all()
	return render(request,'index.html',{'users':users})

def UserReg(request):
	if request.method=='POST':
		firstname=request.POST.get('firstName')
		lastname=request.POST.get('lastName')
		email=request.POST.get('email')
		age=request.POST.get('age')
		gender=request.POST.get('gender')


		user=UserDetails(firstname=firstname,lastname=lastname,email=email,age=age,gender=gender)
		user.save()

		Name=user.firstname+' '+user.lastname
		message=f"{Name},You are successfully created and Registered"
		messages.success(request,message)
		return redirect('home')


def UserEdit(request,pk):
	if request.method=='POST':
		firstname=request.POST.get('firstName')
		lastname=request.POST.get('lastName')
		email=request.POST.get('email')
		age=request.POST.get('age')
		gender=request.POST.get('gender')
		users=UserDetails.objects.filter(user_id=pk).first()

		users.firstname=firstname
		users.lastname=lastname
		users.email=email
		users.age=age 
		users.gender=gender
		users.save()
		Name=users.firstname+' '+users.lastname
		message=f"{Name},You are Data successfully updated"
		messages.success(request,message)
		return redirect('home')


	else:
		userdetail=UserDetails.objects.filter(user_id=pk).values()
		return render(request,'useredit.html',{'userdetail':userdetail})	

	

def SearchUser(request):
	if request.method=='POST':
		name=request.POST.get('search')
		users=UserDetails.objects.filter(firstname__contains=name).values()
		return render(request,'index.html',{'users':users})
	
def DeleteUser(request,pk):
	users=UserDetails.objects.filter(user_id=pk).first()
	Name=users.firstname+' '+users.lastname
	users.delete()
	message=f"{Name},User Successfully Deleted"
	messages.success(request,message)
	return redirect('home')


	