from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StudentForm

# Create your views here.
def home(request):
    return render(request,'studentbackend/index.html')

def studentForm(request):
    if request.method == 'GET':
        return render(request, 'studentbackend/studentform.html')
    if request.method == 'POST':
        data =request.POST
        firstName = data.get('first_name')
        lastName = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        city = data.get('city')
        state = data.get('state')
        country = data.get('country')
        zipCode = data.get('zip_code')
        dateOfBirth = data.get('date_of_birth')
        image = request.FILES.get('image')
        StudentForm.objects.create(
            first_name=firstName,
            last_name=lastName,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            country=country,
            zip_code=zipCode,
            date_of_birth=dateOfBirth,
            image=image,
        )
        return render(request, 'studentbackend/studentform.html', {
            'FirstName': firstName,
            'LastName': lastName,
            'Email': email,
            'Phone': phone,
            'Address': address,
            'City': city,
            'State': state,
            'Country': country,
            'ZipCode': zipCode,
            'DateOfBirth': dateOfBirth
        })

        
def studentList(request):
    students = StudentForm.objects.all()
    return render(request, 'studentbackend/studentData.html', {'students' : students})


def studentDelete(request, id):
    print(id,'delete')
    student = StudentForm.objects.filter(id=id)
    if not student:
        return HttpResponse('Student not found')
    student = StudentForm.objects.get(id=id)
    student.delete()
    return redirect('/studentbackend/student-list/')
    
def studentUpdate(request, id):
    if request.method == 'GET':
        student = StudentForm.objects.filter(id =id)
        if not student:
            return HttpResponse('Student not found')
        student =StudentForm.objects.get(id = id)
        return render(request, 'studentbackend/studentUpdate.html', {'student': student})
    if request.method == 'POST':
        student = StudentForm.objects.filter(id =id)
        if not student:
            return HttpResponse('Student not found')
        student =StudentForm.objects.get(id = id)
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zipCode = request.POST.get('zip_code')
        dateOfBirth = request.POST.get('date_of_birth')
        student.first_name = firstName
        student.last_name = lastName   
        student.email = email
        student.phone = phone
        student.address = address
        student.city = city
        student.state = state
        student.country = country
        student.zip_code = zipCode
        student.date_of_birth = dateOfBirth
        student.save()
        return redirect('/studentbackend/student-list/')
    