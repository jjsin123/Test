from django.db import models
from django.contrib.auth.models import User
import os

# 함수를 사용하는 방법과 class를 사용하는 방법

class Category (models.Model) :
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self) :
        return self.name
    
    def get_absolute_url(self) :
        return f'/blog/category/{self.slug}'
    
    class Meta :
        verbose_name_plural = 'Categories'
    
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100,blank=True)
    content = models.TextField()
    
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d',blank=True)
    # upload_to 는 이미지를 저장 할 경로
    # black=True는 이미지를 저장하지 않고 비워놔도 된다는 뜻
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d',blank=True)
    
    create_at = models.DateTimeField(auto_now_add=True) # 시간이 자동으로 입력
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    category = models.ForeignKey(Category, null=True, blank = True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self): # ext는 확장자를 말함
        return self.get_file_name().split('.')[-1]
    
    
    
    # author : 추후 작성 예정
    
# Create your models here.
