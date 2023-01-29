from django.http import HttpResponse
from django.shortcuts import render
from imit.model import insertdata
from imit.model import mark
import pyodbc

def index(request):
    return render(request,'index.html')

def notices(request):
    return render(request,'notices.html')

def admission(request):
    return render(request,'admission.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=LAPTOP-ESDR60EL\SQLEXPRESS;'
                        'Database=college_website;'
                        'Trusted_Connections=yes;')
    if request.method=="POST":
        insertvalue = insertdata()

        insertvalue.Student_Name = request.POST['StudentName']
        insertvalue.Father_Name = request.POST['FatherName']
        insertvalue.Mother_Name = request.POST['MotherName']
        insertvalue.Course_Name = request.POST['Course']
        insertvalue.Gender = request.POST['Gender']
        insertvalue.Country_Code = int(request.POST['CountryCode'])
        insertvalue.Phone = int(request.POST['Phone'])
        insertvalue.Address = request.POST['CurrentAddress']
        insertvalue.Email = request.POST['Email']
        insertvalue.Password = request.POST['Password']

        cursor = conn.cursor()
        cursor.execute("insert into admission values ('"+insertvalue.Student_Name+"','"+insertvalue.Father_Name+"','"+insertvalue.Mother_Name+"','"+insertvalue.Course_Name+"','"+insertvalue.Gender+"','"+str(insertvalue.Country_Code)+"','"+str(insertvalue.Phone)+"','"+insertvalue.Address+"','"+insertvalue.Email+"','"+insertvalue.Password+"')")
        cursor.commit()
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')
    
def certificate(request):
    dic={}
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=LAPTOP-ESDR60EL\SQLEXPRESS;'
                        'Database=college_website;'
                        'Trusted_Connections=yes;')
    if request.method=="POST":
        uname = request.POST['Username']
        psw = request.POST['Password']
        cursor = conn.cursor()
        cursor.execute("select * from mark")
        result =cursor.fetchall()
        cursor1 = conn.cursor()
        cursor1.execute("select * from admission")
        result1 = cursor1.fetchall()
        dic={'result':result,
             'result1':result1,
            'uname':uname,
            'psw':psw}
    return render(request,'certificate.html',dic)

def facilities(request):
    return render(request,"facilities.html")

def placement(request):
    return render(request,"placement.html")

def library(request):
    return render(request,"library.html")

def computerlab(request):
    return render(request,"computerlab.html")

def ladieshostel(request):
    return render(request,"ladieshostel.html")
    
def boyshostel(request):
    return render(request,"boyshostel.html")