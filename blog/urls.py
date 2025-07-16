from django.urls import path
from . import views

urlpatterns = [
    path('post/delete/<int:pk>/',views.BlogDeleteView.as_view(),name='delete'),
    path('post/<int:pk>/edit/',views.BlogUpdateView.as_view(),name='edit'),
    path('post/create/',views.BlogCreateView.as_view(),name = 'create'),
    path('post/<int:pk>/',views.BlogDetailView.as_view(),name='detail'),
    path('',views.BlogListView.as_view(),name='home')
]
