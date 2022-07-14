from django.shortcuts import redirect, render
from django.views.generic import CreateView

from rest_framework.generics import ListCreateAPIView

from .models import Link
from .serializers import LinkSerializer


class LinkListCreateApiView(ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return self.queryset.filter(user=user)
        else:
            return None


def redirect_view(request, hash):
    link = Link.objects.get(hashed_url=hash)
    response = redirect(link.original_link)
    return response


def link_view(request):
    return render(request, 'link_create.html')
