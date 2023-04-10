from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
from datetime import date
from django.contrib.auth.hashers import make_password , check_password
# Create your views here.

def About(request):
    return render(request,'about.html')

def Index(request):
    return render(request,'index.html')

def contact(request):
    error = ""
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        try:
            Contact.objects.create(name=n, contact=c, email=e, subject=s, message=m, msgdate=date.today(), isread="no")
            error = "no"
        except:
            error = "yes"
    return render(request, 'contact.html', locals())

def adminlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'login.html', locals())

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    dc = Doctor.objects.all().count()
    pc = Patient.objects.all().count()
    ac = Appointment.objects.all().count()

    d = {'dc': dc, 'pc': pc, 'ac': ac}
    return render(request,'admin_home.html', d)

def Logout(request):
    logout(request)
    return redirect('index')

def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=m,special=sp)
            error="no"
        except:
            error="yes"
    return render(request,'add_doctor.html', locals())

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html', d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor.html')

def edit_doctor(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    doctor = Doctor.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        s1 = request.POST['special']

        doctor.name = n1
        doctor.mobile = m1
        doctor.special = s1

        try:
            doctor.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_doctor.html', locals())

def get(request):
    return render(request, 'signup.html')

def signup(request):
    postdata = request.POST
    first_name = postdata.get('firstname')
    last_name = postdata.get('lastname')
    email = postdata.get('email')
    phone = postdata.get('phone')
    password = postdata.get('password')
        # validation
    value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
    }
    patient = Patient(fname=first_name, lname=last_name, mobile=phone, email=email, password=password)
    error_message = validateCustomer(patient)
    if not error_message:
        patient.password = make_password(patient.password)
        patient.register()
        return redirect('homepage')
    else:
        data = {
                'error': error_message,
                'values': value
        }
    return render(request, 'add_patient.html', data)

        
    

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html', d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient.html')

def edit_patient(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    patient = Patient.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        g1 = request.POST['gender']
        a1 = request.POST['address']

        patient.name = n1
        patient.mobile = m1
        patient.gender = g1
        patient.address = a1
        try:
            patient.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_patient.html', locals())



def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html', d)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    d = {'appointment':appointment}
    return render(request,'view_appointment.html', d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment1 = Appointment.objects.get(id=pid)
    appointment1.delete()
    return redirect('view_appointment.html')

def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="no")
    return render(request,'unread_queries.html', locals())

def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="yes")
    return render(request,'read_queries.html', locals())

def view_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.get(id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request,'view_queries.html', locals())

# def get(self, request):
#     return render(request, 'patient_signup.html')

# def post(self, request):
#     postdata = request.POST
#     first_name = postdata.get('firstname')
#     last_name = postdata.get('lastname')
#     phone = postdata.get('phone')
#     password = postdata.get('password')
#     # validation
#     value = {
#             'first_name': first_name,
#             'last_name': last_name,
#             'phone': phone,
#     }
#     customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
#     error_message = self.validateCustomer(customer)
#     if not error_message:
#         print(first_name, last_name, email, password)
#         customer.password = make_password(customer.password)
#         customer.register()

#         return redirect('homepage')
#     else:
#         data = {
#                 'error': error_message,
#                 'values': value
#         }
#         return render(request, 'signup.html', data)

def validateCustomer(patient):
    error_message = None
    if not patient.fname:
        error_message = "First Name Required!!"
    elif len(patient.fname) < 4:
        error_message = "First name must be 4 characters long"
    elif not patient.lname:
        error_message = "Last Name Required!!"
    elif len(patient.lname) < 4:
        error_message = "Last name must be 4 characters long"
    elif not patient.mobile:
        error_message = "Phone number Required!!"
    elif len(patient.mobile) < 10:
        error_message = "phone number must be 10 characters long"
    elif not patient.email:
        error_message = "email required"
    elif len(patient.email) < 2:
        error_message = "give the proper email"
    elif patient.isExists():
        error_message = "Email address is already exists"
    return error_message


