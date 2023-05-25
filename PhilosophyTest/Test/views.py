from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserPersonalInfo, Questions, Test, Answers
from django.db import IntegrityError
from django.http import HttpResponseNotAllowed
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render
from .models import Answers
def home(request):
    return render(request, 'TestLogic/home.html')
#work
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'TestLogic/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']: 
            try:          
                _user = User.objects.create_user(request.POST['username'],password=request.POST['password2'])
                _user.save()
                login(request, _user)     

                user = User.objects.get(username=request.POST['username'])
                user_info = UserPersonalInfo(id_user=user, user_name=request.POST.get("first_name"), 
                                            user_second_name=request.POST.get("second_name"), 
                                            user_father=request.POST.get("father"),
                                            user_group=request.POST.get("num_group"))
                user_info.save()
                return redirect('alltests')
            except IntegrityError:
                return render(request, 'TestLogic/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken. Please choose a new username'})

        else:
            return render(request, 'TestLogic/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})
#work
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

#work
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'TestLogic/loginuser.html',{'form': AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'TestLogic/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('alltests')



def tests(request):
    user_info = UserPersonalInfo.objects.get(id_user=request.user)
    if Answers.objects.filter(userInfo=user_info).exists():        
        return render(request, 'TestLogic/alltests.html', { 'error': "Тест уже выполнен" })
     
    tests = Test.objects.all()
    return render(request, 'TestLogic/alltests.html', {'tests': tests})


#work
def test(request, id):
    questions = Questions.objects.filter(id_test=id)
    return render(request, 'TestLogic/test.html', {'questions': questions})

def save_answers(request):
    if request.method == 'POST':
        for question in request.POST:
            if question.startswith('answer'):
                question_id = int(question.split('answer')[1])
                question_instance = Questions.objects.get(id_question=question_id)
                answer = request.POST[question]
                
                # Затем, при сохранении ответа, используйте полученный экземпляр "question_instance"
                user_personal_info = UserPersonalInfo.objects.get(id_user=request.user)

                answer_instance = Answers(id_questions=question_instance, userInfo=user_personal_info, user_answer=answer)
                answer_instance.save()

        # Другие действия после сохранения ответов
        return redirect('home')  # Перенаправление на страницу после сохранения ответов
    return HttpResponseNotAllowed(['POST'])