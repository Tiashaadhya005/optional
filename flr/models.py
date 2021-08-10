from django.db import models
arr={}
# Create your models here.
class User_lists(models.Model):
    id=models.IntegerField(primary_key=True)
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    Email=models.EmailField()
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    arr[Username]=Password

    def __str__(self):
        return self.Username+" "+self.Password

    # def __str__(self):
    #     return self.Password

    def checkss(username,password):
        d=User_lists.objects.filter(Username=username,Password=password)
        # print(d)
        l=len(d)
        # print(l)
        if l==0:return False
        else:return True
        

