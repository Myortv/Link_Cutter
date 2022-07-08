from django.urls import path, include
from .views import LogInView, SignUpView


urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
