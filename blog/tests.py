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
        
        # 2.1 Post가 존재하지 않는가
        self.assertEqual(Post.objects.count(), 0)
        
        # 2.2 main area에 '아직 게시물이 없습니다'라는 문구가 출력되는가
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다',main_area.text)
        
        # 3.1 포스트가 2개 있다면
        post_001 = Post.objects.create(
            title = '첫번째 포스트입니다.',
            content = 'Hello World. We are the world.',
        )
        
        post_002 = Post.objects.create(
            title = '두번째 포스트입니다.',
            content = '1등이 전부는 아니잖아',
        )
        
        self.assertEqual(Post.objects.count(), 2)
        
        # 3.2 포스트 목록 페이지를 새로고침했을때
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content,'html.parser')
        self.assertEqual(response.status_code, 200)
        
        # 3.3 main area에 포스트가 2개 존재하는가
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        
        # 3.4 '아직 게시물이 없습니다'라는 문구가 더 이상 나타나지 않는가
        self.assertNotIn('아직 게시물이 없습니다',main_area.text)
        
        