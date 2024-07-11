from django.urls import path
from .import views


urlpatterns =[
	path('',views.AdminLogin,name='login'),
	path('home',views.Home,name='home'),
	path('userreg',views.UserReg,name='reg'),
	path('useredit/<pk>',views.UserEdit,name='edit'),
	path('userdetails',views.SearchUser,name='search'),
	path('userdelete/<pk>',views.DeleteUser,name='delete')

]