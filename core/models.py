from django.db import models
from django.contrib.auth.models import User

# Personal Details Model
class PersonalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=False)  # full_name only, no split
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)  # Add this field
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)  # Add this field
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)  # Add this field

    def __str__(self):
        return f'{self.degree} at {self.institution_name}'


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Skill name
    proficiency = models.CharField(max_length=50)  # Proficiency level

    def __str__(self):
        return f"{self.name} - {self.proficiency}"
    
# from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    skills = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return self.name
