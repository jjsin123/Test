from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
# Create your tests here.

class TestView(TestCase): # TestCase에서 상속 받아옴
    def setup(self):
        self.client -= Client()
        
    def test_post_list(self):
        # 1.1 포스트 목록페이지를 가져오는가
        response = self.client.get('/blog/')
            
        # 1.2 정상적으로 페이지가 로드되는가
        self.assertEqual(response.status_code, 200)
            
        # 1.3 페이지 타이틀은 'Blog'인가
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text,'Blog')
            
        # 1.4 네비게이션 바가 있는가
        navbar = soup.nav
            
        # 1.5 Blog, About Me라는 문구가 네비게이션 바에 있는가
        self.assertIn('Blog',navbar.text)
        self.assertIn('About Me',navbar.text)