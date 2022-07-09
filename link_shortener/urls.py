from django.urls import path

from .views import LinkListCreateApiView, redirect_view


urlpatterns = [
    path('api/link', LinkListCreateApiView.as_view()),
    path('<str:hash>/', redirect_view, name='redirect')
]
