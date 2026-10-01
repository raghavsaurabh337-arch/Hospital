from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Doctor, Patient

# Create your views here.
def home(request):
    if request.method == "POST":
        patient_name = request.POST['patient_name']
        father_name = request.POST['father_name']
        age = request.POST['age']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address = request.POST['address']
        problem = request.POST['problem']

        # Create and save the patient object
        patient = Patient.objects.create(
            patient_name=patient_name,
            father_name=father_name,
            age=age,
            gender=gender,
            mobile=mobile,
            address=address,
            problem=problem
        )
        return redirect('patient_list') # Redirect to the patient list page after successful form submission
    doctors = Doctor.objects.all()
  
     
    
    return render(request, "home.html", {'doctors': doctors})
def doctor_detail(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, "doctor_detail.html", {'doctor': doctor})

def patient_list(request):
    
    patients = Patient.objects.all()
    for patient in patients:
        patient.patient_name = patient.patient_name.capitalize()
        patient.father_name = patient.father_name.capitalize()
        patient.problem = patient.problem.capitalize()
        patient.address=patient.address.capitalize()
    return render(request, "patient.html", {'patients': patients})


