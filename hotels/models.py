from django.db import models

class Hotel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
