from django.urls import path
from . import views
from .views import SignupPageView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup')
]