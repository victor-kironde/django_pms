from django.test import TestCase
from .models import Category, Product
from django.contrib.auth.models import User
from django.core import mail
from django.test.utils import override_settings
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from .views import UserFormView, IndexView, ProductCreate, DetailView
from unittest.mock import patch, MagicMock


class PMSTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="TestCategory", description="Test Description")
        Product.objects.create(name="MyProduct", price=4, quantity=1,
                               category=Category.objects.get(name="TestCategory"))
        self.category = Category.objects.get(name="TestCategory")
        self.product = Product.objects.get(name="MyProduct")
        self.user = User.objects.create_user(username='testuser', password='12345')

        request = RequestFactory()
        request.user = self.user
        self.factory = RequestFactory()

    def test_product_is_created_successfully(self):
        self.assertEqual(self.product.name, "MyProduct")

    def test_category_is_created_successfully(self):
        self.assertEqual(self.category.name, "TestCategory")

    def test_product_has_a_category(self):
        self.assertEqual(self.product.category, self.category)

    def test_user_login(self):
        login = self.client.login(username='testuser', password='12345')
        self.assertIn('_auth_user_id', self.client.session)

    def test_product_string_representation(self):
        self.assertEqual(str(self.product), self.product.name)

    def test_product_string_representation(self):
        self.assertEqual(str(self.product), self.product.name)

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), self.category.name)

    # @override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
    # def test_send_email(self):
    #     mail_sent_success = mail.send_mail('Subject here',
    #                                        'Here is the message.',
    #                                        '', ['victa2015@gmail.com'],
    #                                        fail_silently=False)
    #     self.assertEquals(mail_sent_success, 1)

    def test_user_get_registration_view(self):
        request = self.factory.get(reverse('core:register'))
        response = UserFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        request = self.factory.get(reverse('core:index'))
        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_product_create_view(self):
        request = self.factory.get(reverse('core:product-add'))
        response = ProductCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)

    # @patch('pms.core.models.Product.save', MagicMock(name="save"))
    # def test_create_product(self):
    #
    #     # Create the request
    #     data = {
    #         'name': 'My Product',
    #         'quantity': 49,
    #         'category': self.category,
    #         'price': 5
    #     }
    #     request.user = self.user
    #     request = self.factory.post(reverse('core:product'), data)
    #     # Get the response
    #     response = DetailView.as_view()(request)
    #     self.assertEqual(response.status_code, 302)
    #     # Check save was called
    #     self.assertTrue(Product.save.called)
    #     self.assertEqual(Product.save.call_count, 1)
