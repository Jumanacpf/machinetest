from django.db import models

# Create your models here.


class Register(models.Model):
    first_name=models.CharField(max_length=40,null=True)
    last_name = models.CharField(max_length=40, null=True)
    username = models.CharField(max_length=40, null=True)
    email=models.EmailField(max_length=40,null=True)
    address=models.CharField(max_length=100,null=True)
    phone=models.IntegerField(null=True)
    password=models.IntegerField(null=True)

    def __str__(self):
        return self.username


class Blog(models.Model):
    register_id=models.ForeignKey(Register,on_delete=models.CASCADE)
    title=models.CharField(max_length=40, null=True)
    image=models.FileField(null=True)
    description=models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.title

