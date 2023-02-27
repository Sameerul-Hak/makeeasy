from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=50)
    conform_password=models.CharField(max_length=50)

    def __str__(self):
        return self.name