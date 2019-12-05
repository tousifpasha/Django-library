from .serializer import BookSerializer,BookCreateSerializer,BookDestroySerializer,BookUpdateSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from .models import Book

class BookListAPIView(ListAPIView):

    queryset=Book.objects.all()
    serializer_class=BookSerializer


class BookCreateAPIView(CreateAPIView):

    queryset=Book.objects.all()
    serializer_class=BookCreateSerializer
    
class BookDestroyAPIView(DestroyAPIView):

    queryset=Book.objects.all()
    serializer_class=BookDestroySerializer
    lookup_field='pk'

class BookUpdateAPIView(UpdateAPIView):

    queryset=Book.objects.all()
    serializer_class=BookUpdateSerializer
    lookup_field='pk'
