from django.db.models.base import Model
from django.forms import ModelForm
from .models import MovieComment, Review, ReviewComment, Quiz

class MovieCommentForm(ModelForm):
    class Meta:
        model = MovieComment
        fields = ('grade', 'content')
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('title','content','draw')
        
class ReviewCommentForm(ModelForm):
    class Meta:
        model = ReviewComment
        fields = ('content',)
        
class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ('movie', 'draw')