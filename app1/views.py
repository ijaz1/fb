from django.shortcuts import render
from . models import*

# Create your views here.

def signupfn(request):
    return render(request,'index.html')

def afun(requuest):
    return render(requuest,'active.html')    

def ffun(request):
    return render(request,'firstpage.html')    

def lifun(request):
    return render(request,'link.html')

def actfun(request):
    return render(request,'account.html')

def usfn(request):
    return render(request,'editprofile.html')    

def chfn(request):
    return render(request,'change.html')

def signup(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        surname=request.POST['surname']
        emailorphone=request.POST['emailorphone']
        username=lgin.objects.filter(email=emailorphone).exists()
        if username==False:
            password=request.POST['password']
            day=request.POST['day']
            print(day)
            month=request.POST['month']
            year=request.POST['year']
            dateofbirth=year+'-'+month+'-'+day
            gender=request.POST['i']
            obj=lgin(fname=firstname,sname=surname,email=emailorphone,gender=gender,crpassword=password,dateofbirth=dateofbirth)
            obj.save()
            return render(request,'account.html',{'msg1':'Sign up succesful'})
        return render(request,'index.html',{'msg':'it,s already exist'})
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        try:
            username=request.POST['loginusername']
            print(username)
            password=request.POST['loginpassword']
            print(password)
            obj=lgin.objects.get(email=username,crpassword=password)
            print(obj)
            request.session['ses']=obj.id
            obj1=lgin.objects.get(id=obj.id)
            print(obj1)

            return render(request,'account.html',{'msg2':obj1})
        except Exception as e:print(e)
    return render(request,'index.html',{'msg3':'invalid username'})

def chfn(request):
    if request.method=='POST':
        try:
            oldpass=request.POST['oldpassword']
            print(oldpass)
            newpass=request.POST['newpassword']
            print(newpass)
            obj3=request.session['ses']
            print(obj3)
            obj4=lgin.objects.get(id=obj3)
            print(obj4)
            if obj4.crpassword==oldpass:
                obj4.crpassword=newpass
                obj4.save()
                return render(request,'change.html',{'msge':{'password changed succesfully'}})
            return render(request,'change.html',{'msg4':'old password is wrong'})  
        except Exception as e:print(e)
    return render(request,'change.html')

def usfn(request):
    if request.method=='POST':
        try:
            fname=request.POST['fname']
            sname=request.POST['sname']
            email=request.POST['email']
            day=request.POST['day']
            month=request.POST['month']
            year=request.POST['year']
            dateofbirth=year+'-'+month+'-'+day
            ob=request.session['ses']
            ob1=lgin.objects.get(id=ob)
            ob1.fname=fname
            ob1.sname=sname
            ob1.email=email
            ob1.dateofbirth=dateofbirth
            ob1.save()
            return render(request,'editprofile.html',{'msms':'updated successfully'})
        except Exception as e:print(e)
    return render(request,'editprofile.html',{'msmsm':'something went wrong'})




