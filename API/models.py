from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    experience = models.IntegerField()
    department = models.CharField(max_length=100)
    timing = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="doctors/", blank=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other"),
        ]
    )

    
    mobile = models.CharField(max_length=15)

    address = models.TextField()
    problem = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.patient_name