from django.urls import path

from .views import LinkListCreateApiView


urlpatterns = [
    path('cut', LinkListCreateApiView.as_view()),
    # path('api/link/', LinkRetrieveApiView.as_view(), name='api-link')
]
