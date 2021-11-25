from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('choice/', views.choice, name="choice"),
    
    path('index/<int:mode>/', views.index, name="index"),
    
    path('detail/<int:movie_pk>/', views.detail, name="detail"),
    path('movie_comment/<int:movie_pk>/', views.movie_comment, name="movie_comment"),
    path('movie_comment_delete/<int:comment_pk>/<int:movie_pk>/', views.movie_comment_delete, name="movie_comment_delete"),
    
    path('review_create/<int:movie_pk>/', views.review_create, name="review_create"),
    path('review/<int:review_pk>/', views.review, name="review"),
    path('review_update/<int:review_pk>/', views.review_update, name="review_update"),
    path('review_delete/<int:movie_pk>/<int:review_pk>/', views.review_delete, name="review_delete"),
    path('review_comment/<int:review_pk>/', views.review_comment, name="review_comment"),
    path('review_comment_delete/<int:review_pk>/<int:review_comment_pk>/', views.review_comment_delete, name="review_comment_delete"),
    
    path('usercolor_create/', views.usercolor_create, name="usercolor_create"),
    path('usercolor_update/<rgb>/', views.usercolor_update, name="usercolor_update"),
    
    path('voice_process/', views.voice_process, name="voice_process"),    
    
    path('quiz_create/', views.quiz_create, name="quiz_create"),
    path('quiz/', views.quiz, name="quiz"),
    path('quiz_check/', views.quiz_check, name="quiz_check"),
]
