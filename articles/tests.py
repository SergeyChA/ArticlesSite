from django.test import TestCase


class SimpleTests(TestCase):
    def test_admin_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 403)

    def test_home_page_status_code(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get('/articles/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_code(self):
        response = self.client.get('/articles/login/')
        self.assertEqual(response.status_code, 200)        

    def test_account_page_status_code(self):
        response = self.client.get('/articles/account/')
        self.assertEqual(response.status_code, 200)

    def test_tags_page_status_code(self):
        response = self.client.get('/articles/tags/')
        self.assertEqual(response.status_code, 200) 

    def test_tag_create_page_status_code(self):
        response = self.client.get('/articles/tag/create/')
        self.assertEqual(response.status_code, 403)

    def test_article_create_page_status_code(self):
        response = self.client.get('/articles/article/create/')
        self.assertEqual(response.status_code, 403) 

    def test_article_update_page_status_code(self):
        response = self.client.get('/articles/article/<str:slug>/update/')
        self.assertEqual(response.status_code, 403)

    def test_tag_update_page_status_code(self):
        response = self.client.get('/articles/tag/<str:slug>/update/')
        self.assertEqual(response.status_code, 403)

    def test_article_detail_page_status_code(self):
        response = self.client.get('/articles/article/<str:slug>/update/')
        self.assertEqual(response.status_code, 403)

    def test_tag_delete_page_status_code(self):
        response = self.client.get('/articles/tag/<str:slug>/delete/')
        self.assertEqual(response.status_code, 403)

    def test_article_delete_page_status_code(self):
        response = self.client.get('/articles/tag/<str:slug>/delete/')
        self.assertEqual(response.status_code, 403)






