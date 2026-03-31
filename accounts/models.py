from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICE =(
        ('candidate','Candidate'),
        ('recruiter','Recruiter'),
        ('admin','Admin'),
    )

    role = models.CharField(max_length=20,choices=ROLE_CHOICE,default='candidate')

    def __str__(self):
        return f"{self.role} : {self.username}"



