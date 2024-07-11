from django.db import models


#User Table
class UserDetails(models.Model):
	user_id=models.AutoField(db_index=True,primary_key=True)
	firstname=models.CharField(db_index=True,max_length=250)
	lastname=models.CharField(db_index=True,max_length=250,null=True)
	email=models.EmailField(db_index=True,max_length=250,unique=True)
	age=models.IntegerField(db_index=True)
	gender=models.CharField(db_index=True,max_length=100)

	def __str__(self):
		return self.firstname+self.lastname

	class Meta:
		db_table="UserDetails"



