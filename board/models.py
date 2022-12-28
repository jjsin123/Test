from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=150)
    content = MarkdownxField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'
    
    def get_absolute_url(self):
        return f'/board/{self.pk}/'
    
    def get_content_markdown(self):
        return markdown(self.content)
    

    
class Board_Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.author}::{self.content}'
    
    
    def get_absolute_url(self):
        return f'{ self.board.get_absolute_url()}#comment-{self.pk}'