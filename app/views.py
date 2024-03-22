from django.shortcuts import render
from . forms import HospitalForm
from . models import Department,Doctor
def index(request):
    department=Department.objects.all()
    doctor=Doctor.objects.all()
    form=HospitalForm()
    context={
        "department":department,
        "doctor":doctor,
        "form":form
    }
    if request.method=="POST":
        data=HospitalForm(request.POST)
        if data.is_valid():
            data.save()
            form=HospitalForm()
            return render(request,"index.html",context)
    return render(request,"index.html",context)
