from .models import Board, Board_Comment
from django import forms

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','content']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Board_Comment
        fields = ('content', )