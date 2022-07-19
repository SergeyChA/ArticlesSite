from django.test import TestCase


class SimpleTests(TestCase):
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






