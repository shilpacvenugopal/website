from django.db import models

# Create your models here.
from django.db import models

class InvestorQuery(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    area_of_interest = models.CharField(max_length=150)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Job(models.Model):
    CATEGORY_CHOICES = [
        ('developer', 'Developer'),
        ('marketing', 'Marketing'),
        ('designer', 'Designer'),
        ('sales', 'Sales'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.category})"
    


class JobApplication(models.Model):
    role = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    qualification = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.role}"

