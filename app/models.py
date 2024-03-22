from django.db import models

class Department(models.Model):
    dep_name=models.TextField(max_length=100)
    dep_descp=models.TextField(max_length=200)
    def __str__(self):
        return self.dep_name

class Doctor (models.Model):
    doc_name=models.TextField(max_length=100)
    doc_spec=models.TextField(max_length=100)
    doc_image=models.ImageField(upload_to="image")
    doc_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.doc_name
class Hospital(models.Model):
    name=models.TextField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    problem=models.TextField(max_length=200)
    def __str__(self):
        return self.name
