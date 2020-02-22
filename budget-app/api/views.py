from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import BudgetSerializer, ItemSerializer, AuthSerializer, RegistrationSerializer
from .models import Budget

# Create your views here.
class CreateView(generics.CreateAPIView):
    serializer_class = BudgetSerializer

class CreateItemView(generics.CreateAPIView):
    serializer_class = ItemSerializer

class RetrieveView(generics.RetrieveAPIView):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()

class LoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = AuthSerializer

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
