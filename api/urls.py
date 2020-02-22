from django.urls import path
from . import views

app_name = 'budgetapp'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('create/', views.CreateView.as_view(), name='create_view'),
    path('budget_item/', views.CreateItemView.as_view(), name='budget_item'),
    path('budget/<int:pk>/', views.RetrieveView.as_view(), name='retrieve_view'),
]
