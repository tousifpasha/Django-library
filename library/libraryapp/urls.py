from django.urls import path
from .views import BookListAPIView, BookCreateAPIView,BookDestroyAPIView,BookUpdateAPIView

urlpatterns = [

    path('book/',BookListAPIView.as_view(), name='book_list'),
    path('create/',BookCreateAPIView.as_view(), name='create_book'),
    path('destroy/<int:pk>/',BookDestroyAPIView.as_view(), name='destroy_book'),
    path('update/<int:pk>/',BookUpdateAPIView.as_view(), name='update_book'),
    
]