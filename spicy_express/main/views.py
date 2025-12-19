from django.http import JsonResponse
from .models import Feedback
from .forms import FeedbackForm
from django.shortcuts import render, redirect

# Основные страницы
def index(request):
    return render(request, 'main/index.html')

def restaurants(request):
    return render(request, 'main/restaurants.html')

def main_page(request):
    return render(request, 'main/main.html')

def jobs(request):
    return render(request, 'main/jobs.html')

def account(request):
    return render(request, 'main/account.html')

def promotions(request):
    return render(request, 'main/promotions.html')

def menu(request):
    return render(request, 'main/menu.html')

def home(request):
    return render(request, 'main/home.html')

def home(request):
    return render(request, 'main/home.html')

def feedback_form(request):
    return render(request, 'main/feedback_form.html')  # HTML-файл с формой

#FEEDBACK
from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'main/feedback_form.html', {'form': form})

def feedback_success(request):
    return render(request, 'main/feedback_success.html')


from django.shortcuts import render
from .models import Feedback

def question_list(request):
    feedbacks = Feedback.objects.all().order_by('-submitted_at')  # Получаем все записи из Feedback
    return render(request, 'main/question_list.html', {'feedbacks': feedbacks})  # Передаём в шаблон



#REGGISTRATION/AUTH
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # После успешной регистрации перенаправляем на страницу входа
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})

# Авторизация
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('account')  # Перенаправляем в личный кабинет
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

# Личный кабинет
@login_required
def account(request):
    return render(request, 'main/account.html', {'user': request.user})

# Выход
def user_logout(request):
    logout(request)
    return redirect('login')


