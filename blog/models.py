from django.db import models

# 함수를 사용하는 방법과 class를 사용하는 방법

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d',blank=True)
    # upload_to 는 이미지를 저장 할 경로
    # black=True는 이미지를 저장하지 않고 비워놔도 된다는 뜻
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d',blank=True)
    create_at = models.DateTimeField(auto_now_add=True) # 시간이 자동으로 입력
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    # author : 추후 작성 예정
    
# Create your models here.
