from django.urls import path

from .views import (
                LinkListCreateApiView,
                redirect_view,
                link_view,
                LinkListView
            )


urlpatterns = [
    path('api/link', LinkListCreateApiView.as_view(), name='api'),
    path('<str:hash>/', redirect_view, name='redirect'),
    path('cut', link_view, name='cut-link'),
    path('mylinks', LinkListView.as_view(), name='my_links'),
    path('', link_view, name='home')

]
