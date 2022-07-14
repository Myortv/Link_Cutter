from django.urls import path

from .views import LinkListCreateApiView, redirect_view, link_view


urlpatterns = [
    path('api/link', LinkListCreateApiView.as_view(), name='api'),
    path('<str:hash>/', redirect_view, name='redirect'),
    path('cut', link_view, name='cut'),
]
