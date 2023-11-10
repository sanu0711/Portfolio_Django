from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Student,Question,Result,Option,StudentSubmission
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta
# Create your views here.
global current_time
def signup(request):
    if request.method == 'POST':
        n=request.POST['name']
        u=request.POST['username']
        e=request.POST['email']
        ph=request.POST['phone']
        p=request.POST['password']
        stu=Student(user=u,phone=ph, password=p,email=e, name=n)
        usr = User.objects.create_user(username=u, password=p,email=e, first_name=n)
        usr.save()
        stu.save()
        
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        u=request.POST['username']
        p=request.POST['password']
        user = auth.authenticate(username=u, password=p)
        if user is not None:
            auth.login(request, user)
            global current_time
            current_time = datetime.now()
            return redirect('quizdashboard')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url='login')
def quizdashboard(request):
    global current_time
    start_time=current_time + timedelta(minutes=1)
    if start_time < datetime.now():
        global t
        t=-1
        return redirect('quiz')
    else:
        wait=(start_time-datetime.now()).seconds
        data={"Start_in":start_time,'wait':wait}
        return render(request,'quizdashboard.html',data)
    

# @ user_passes_test()  write a function to check if user is authenticated or not
@login_required(login_url='login')
def quiz(request):
    global t
    qus=Question.objects.all()
    answ=[i.answer for i in qus]
    std=Student.objects.get(user=request.user)
    if std.score>=10:
                std.score=0
                std.save()
    if request.method == 'POST':
        ans=request.POST['ans']
        def check():
            if ans in answ:
                return True
            else:
                return False
        
        stusub=StudentSubmission(user=request.user,questionNo=t+1,submittime=datetime.now(),status=check())
        stusub.save()
        if ans in answ:
            std.score+=1
            opt=Option(user=request.user,option=ans)
            rt=Result(user=request.user,score=std.score)
            opt.save()
            std.save()
            rt.save()
        return redirect('quiz')
    qust=[i.question for i in qus]
    o1=[i.option1 for i in qus]
    o2=[i.option2 for i in qus]
    o3=[i.option3 for i in qus]
    o4=[i.option4 for i in qus]
    t+=1
    if t==len(qus):
        t=0
        return redirect('result')
    data={"question":qust[t],"option1":o1[t],"option2":o2[t],"option3":o3[t],"option4":o4[t],"timeleft":25}
    return render(request,'quiz.html',data)

@login_required(login_url='login')
def result(request):
    std=Student.objects.get(user=request.user)
    opt=Option.objects.filter(user=request.user)
    stusubm=StudentSubmission.objects.filter(user=request.user)
    data={"name":std.name,"score":std.score,"option":opt,"stusubm":stusubm}

    return render(request,'Quizend.html',data)