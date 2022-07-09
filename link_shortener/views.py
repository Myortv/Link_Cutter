from rest_framework.generics import ListCreateAPIView
# from rest_framework import filters
from django.views.generic import CreateView

# from django_filters.rest_framework import DjangoFilterBackend

from .models import Link
from .serializers import LinkSerializer

# class LinkCreateView(CreateView):
#     model = Link
#     template_name = 'shortener'
#     form_class = LinkCreationForm
#     success_url = None
#
#     def post(request, *args, **kwargs):

# class LinkRetrieveApiView(RetrieveAPIView):
#     queryset = Link.objects.all()
#     serializer_class = LinkSerializer

    #
    # def perform_create(self, serializer):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         serializer.save()


class LinkListCreateApiView(ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get_queryset(self):
        return self.queryset.filter(users=self.request.user)
