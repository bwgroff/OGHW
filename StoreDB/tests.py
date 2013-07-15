from django.test.client import Client
from django.test import TestCase
from django.contrib.auth.models import User


class OGHWTestCase(TestCase):
    fixtures = ['StoreDB_views_testdata.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser', password='12345', 
                                        is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('hello')
        self.user.save()
        self.assertTrue(self.client.login(username='testuser',password='hello'))

    def tearDown(self):
        self.user.delete()

    def test_login(self):
        self.assertTrue(self.client.login(username='testuser',password='hello'))
        self.client.logout()
        self.assertFalse(self.client.login(username='x', password='y'))
        self.client.logout()

    def test_landing_page(self):
        '''
        sends various requests to /
        '''
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_for_404(self):
        '''
        pings some addresses that should yield 404
        '''
        self.assertEqual(self.client.get('/acx').status_code, 404)
        self.assertEqual(self.client.get('/accounts/').status_code, 404)
        self.assertEqual(self.client.get('/profile/').status_code, 404)
        self.assertEqual(self.client.get('/product_page').status_code, 404)
        self.assertEqual(self.client.get('/product_page/').status_code, 404)

    def test_order_history_nologin(self):
        '''
        tests the history view without any user authenticated
        '''
        self.client.logout()
        self.assertEqual(self.client.get('history').status_code, 404)
        self.assertEqual(self.client.get('/history').status_code, 200)
        self.assertEqual(len(self.client.get('/history').context),2)
        self.assertEqual(self.client.get('/history').content[-43:-32],'valid query')

    def test_order_history_login(self):
        '''
        tests the history view with a user authenticated
        '''
        self.client.login(username='testuser',password='hello')
        self.assertEqual(self.client.get('history').status_code, 404)
        self.assertEqual(self.client.get('/history').status_code, 200)
        self.assertFalse(self.client.get('/history').content[-43:-32]=='valid query')
        self.client.logout()

    def test_product_page(self):
        self.client.logout()
        response1 = self.client.get('/product_page/0x0/')
        response2 = self.client.get('/product_page/1/')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertFalse('<form' in response1.content)
        self.assertFalse('<form' in response2.content)

        self.client.login(username='testuser', password='hello')
        response1 = self.client.get('/product_page/0x0/')
        response2 = self.client.get('/product_page/1/')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertFalse('<form' in response1.content)
        self.assertTrue('<form' in response2.content)

        self.client.logout()

    def test_purchase_page(self):
        self.client.logout()
        response1 = self.client.get('/purchase/x/x')
        response2 = self.client.get('/purchase/x/?q=6')
        response3 = self.client.get('/purchase/1/x')
        response4 = self.client.get('/purchase/1/?q=3')
        response5 = self.client.get('/purchase/1/?q=-3')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(response5.status_code, 200)

        self.assertTrue('Oops' in response1.content)
        self.assertTrue('Oops' in response2.content)
        self.assertTrue('Oops' in response3.content)
        self.assertTrue('Oops' in response4.content)
        self.assertTrue('Oops' in response5.content)

        self.client.login(username='testuser', password='hello')
        response1 = self.client.get('/purchase/x/x')
        response2 = self.client.get('/purchase/x/?q=6')
        response3 = self.client.get('/purchase/1/x')
        response4 = self.client.get('/purchase/1/?q=3')
        response5 = self.client.get('/purchase/1/?q=-3')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(response5.status_code, 200)

        self.assertTrue('Oops' in response1.content)
        self.assertTrue('Oops' in response2.content)
        self.assertTrue('Oops' in response3.content)
        self.assertFalse('Oops' in response4.content)
        self.assertTrue('Oops' in response5.content)
