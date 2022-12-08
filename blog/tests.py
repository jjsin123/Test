from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import Post
# Create your tests here.

class TestView(TestCase): # TestCase에서 상속 받아옴
    def setUp(self):
        self.client = Client()
        self.user_trump = User.objects.create_user(username='trump',password='somepassword')
        self.user_james = User.objects.create_user(username='james',password='somepassword')
        
    def navbar_test(self,soup):
        navbar = soup.nav
        self.assertIn('Blog',navbar.text)
        self.assertIn('About Me',navbar.text)
        
        logo_btn = navbar.find('a', text="Do It Django")
        self.assertEqual(logo_btn.attrs['href'],'/')
        
        home_btn = navbar.find('a', text="Home")
        self.assertEqual(logo_btn.attrs['href'],'/')
        
        blog_btn = navbar.find('a', text="Blog")
        self.assertEqual(logo_btn.attrs['href'],'/blog/')
        
        about_me_btn = navbar.find('a', text="About Me")
        self.assertEqual(logo_btn.attrs['href'],'/about_me/')
        
        
        
    def test_post_list(self):
        # 1.1 포스트 목록페이지를 가져오는가
        response = self.client.get('/blog/')
            
        # 1.2 정상적으로 페이지가 로드되는가
        self.assertEqual(response.status_code, 200)
            
        # 1.3 페이지 타이틀은 'Blog'인가
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text,'Blog')
#        self.navbar_test(soup)
        
        # 2.1 Post가 존재하지 않는가
        self.assertEqual(Post.objects.count(), 0)
        
        # 2.2 main area에 '아직 게시물이 없습니다'라는 문구가 출력되는가
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다',main_area.text)
        
        # 3.1 포스트가 2개 있다면
        post_001 = Post.objects.create(
            title = '첫번째 포스트입니다.',
            content = 'Hello World. We are the world.',
            author = self.user_trump
        )
        
        post_002 = Post.objects.create(
            title = '두번째 포스트입니다.',
            content = '1등이 전부는 아니잖아',
            author = self.user_james
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
        
        self.assertIn(self.user_trump.username.upper(),main_area.text)
        self.assertIn(self.user_james.username.upper(),main_area.text)    
        
    def test_post_detail(self):
        # 1.1 포스트가 하나 존재하는가
        post_001 = Post.objects.create(
            title = '첫번째 포스트입니다.',
            content = 'Hello World. We are the world.',
            author = self.user_trump,
        )
    
        # 1.2 그 포스트 url은 '/blog/1/'의 형식인가
        self.assertEqual(post_001.get_absolute_url(), '/blog/1/')
    
        # 2 첫번째 포스트의 상세페이지
        # 2.1 첫번째 포스트의 url로 접근하면 정상적으로 작동하는가(status code : 200)
        response = self.client.get(post_001.get_absolute_url())
        soup = BeautifulSoup(response.content,'html.parser')
        self.assertEqual(response.status_code, 200)
    
        # 2.2 포스트 목록페이지와 같은 navbar가 존재하는가
#        self.navbar_test(soup)
        
        # 2.3 첫번째 포스트의 제목이 웹브라우저 탭 타이틀에 존재하는가
        self.assertIn(post_001.title, soup.title.text)
        
        # 2.4 첫번째 포스트의 제목이 포스트 영역에 존재하는가
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area')
        self.assertIn(post_001.title, post_area.text)  
    
        # 2.5 첫번째 포스트의 작성자가 포스트 영역에 존재하는가
        self.assertIn(self.user_trump.username.upper(),post_area.text)
    
        # 2.6 첫번째 포스트의 내용이 포스트 영역에 존재하는가
        self.assertIn(post_001.content, post_area.text)
        