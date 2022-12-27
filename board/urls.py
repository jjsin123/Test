from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.BoardCreate.as_view()),
    path('<int:pk>/',views.BoardDetail.as_view()),
    path('',views.BoardList.as_view()),
    path('delete_board/<int:pk>/', views.delete_board),
    
    
    
    path('update_board/<int:pk>/',views.BoardUpdate.as_view()),
]