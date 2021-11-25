from django.db import models
from django.conf import settings
from django.db.models.fields import CharField, related

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    poster_url = models.TextField(null=True)
    naver_grade = models.FloatField(null=True)
    user_grade = models.IntegerField(null=True)
    release_date = models.TextField()
    trailer_url = models.TextField(null=True)

    def __str__(self):
        return self.title

class Color(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, null=True) # Main Color
    color_url = models.TextField(null=True) # Frame 
    color_1_R = models.CharField(max_length=50)
    color_1_G = models.CharField(max_length=50)
    color_1_B = models.CharField(max_length=50)
    color_2_R = models.CharField(max_length=50)
    color_2_G = models.CharField(max_length=50)
    color_2_B = models.CharField(max_length=50)
    color_3_R = models.CharField(max_length=50)
    color_3_G = models.CharField(max_length=50)
    color_3_B = models.CharField(max_length=50)
    color_4_R = models.CharField(max_length=50)
    color_4_G = models.CharField(max_length=50)
    color_4_B = models.CharField(max_length=50)
    color_5_R = models.CharField(max_length=50)
    color_5_G = models.CharField(max_length=50)
    color_5_B = models.CharField(max_length=50)
    
    def __str__(self):
        return self.movie.title
    
class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    grade = models.IntegerField()
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    draw = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class UserColorRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    
class Quiz(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=13)
    draw = models.ImageField(blank=True, upload_to='images/')
    correct_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="corrected_quizs")