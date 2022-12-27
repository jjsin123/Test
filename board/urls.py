from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.BoardCreate.as_view()),
    path('<int:pk>/',views.BoardDetail.as_view()),
    path('',views.BoardList.as_view()),
    path('delete_board/<int:pk>/', views.delete_board),
    path('update_board/<int:pk>/',views.BoardUpdate.as_view()),
    
    
    path('delete_comment/<int:pk>/',views.delete_comment),    
    path('update_comment/<int:pk>/',views.CommentUpdate.as_view()),    
    path('<int:pk>/new_comment/',views.new_comment),
]