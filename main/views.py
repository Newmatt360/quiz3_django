from django.shortcuts import render
from .models import Student

def home(request):
    if not Student.objects.filter(first_name="Alonzo").exists():
        Student.objects.all().delete()
        Student.objects.create(first_name="Alonzo", last_name="Sean", age=20, email="alonzosean@email.com", course="BSIT")
        Student.objects.create(first_name="Christian Abuel", last_name="Perlada", age=20, email="christian.perlada@email.com", course="BSIT")
        Student.objects.create(first_name="Christian Lenard", last_name="Melecia", age=20, email="christian.melecia@email.com", course="BSIT")
        Student.objects.create(first_name="Clark", last_name="Sepillo", age=20, email="clark.sepillo@email.com", course="BSIT")
        Student.objects.create(first_name="Dishiela Ingrid", last_name="Camunag", age=20, email="dishiela.camunag@email.com", course="BSIT")
        Student.objects.create(first_name="ED", last_name="Domanico", age=20, email="ed.domanico@email.com", course="BSIT")
        Student.objects.create(first_name="Edriane Paul", last_name="Domanico", age=20, email="edriane.domanico@email.com", course="BSIT")

    students = Student.objects.all()
    return render(request, 'main/home.html', {'students': students})