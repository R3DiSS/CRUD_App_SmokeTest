# from django.test import TestCase
# from .models import Articles  

# class ArticlesViewTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         Articles.objects.create(title='Test Title', anons='Test Anons', full_text='Test Body', date='2023-09-16T00:00')

#     def test_news_home_view(self):
#         response = self.client.get('/news/')
#         self.assertEqual(response.status_code, 200)

#     def test_news_detail_view(self):
#         article = Articles.objects.get(id=1)
#         response = self.client.get(article.get_absolute_url())
#         self.assertEqual(response.status_code, 200)

#     def test_news_create_view(self):
#         response = self.client.get('/news/create')
#         self.assertEqual(response.status_code, 200)
        

# from django.test import TestCase
# from django.urls import reverse
# from .models import Articles

# class NewsTestCase(TestCase):
#     def setUp(self):
#         Articles.objects.create(title="Test Title", anons="Test Anons", full_text="Test full text")
        
#     def test_news_list(self):
#         response = self.client.get(reverse('news_home'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Test Title")

#     def test_article_creation(self):
#         article = Articles.objects.get(title="Test Title")
#         self.assertIsNotNone(article)

    
from django.test import TestCase
from django.urls import reverse
from .models import Articles

class NewsSmokeTest(TestCase):

    def setUp(self):
        self.article = Articles.objects.create(
            title='Test Title',
            anons='Test Anons',
            full_text='Test Full Text',
            date='2022-01-01T10:20:30Z'
        )

    def test_news_home_view(self):
        response = self.client.get(reverse('news_home'))
        self.assertEqual(response.status_code, 200)

    def test_news_detail_view(self):
        response = self.client.get(reverse('news-detail', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)

    def test_news_create_view(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)

    def test_news_update_view(self):
        response = self.client.get(reverse('news-update', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)

    def test_news_delete_view(self):
        response = self.client.get(reverse('news-delete', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
