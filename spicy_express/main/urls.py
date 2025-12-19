from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('restaurants/', views.restaurants, name='restaurants'),  # Страница ресторанов
    path('main/', views.main_page, name='main_page'),  # Главная страница main
    path('jobs/', views.jobs, name='jobs'),  # Страница вакансий
    path('account/', views.account, name='account'),  # Личный кабинет
    path('menu/', views.menu, name='menu'),  # Меню
    path('promotions/', views.promotions, name='promotions'),  # Акции
    path('home/', views.home, name='home'),
    path('feedback/', views.feedback_form, name='feedback_form'),  # Страница с формой обратной связи
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),  # Обработка формы
    path('feedback-success/', views.feedback_success, name='feedback_success'),  # Страница успеха
    path('questions/', views.question_list, name='question_list'),    
    path('register/', views.register, name='register'), # Страница регистрации
    path('login/', views.user_login, name='login'), # Страница входа
    path('logout/', views.user_logout, name='logout'), # Страница выхода
]