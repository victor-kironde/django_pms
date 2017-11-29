from django.test import TestCase
from .models import Category, Product
from django.contrib.auth.models import User


class PMSTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="TestCategory", description="Test Description")
        Product.objects.create(name="MyProduct", price=4, quantity=1,
                               category=Category.objects.get(name="TestCategory"))
        self.category = Category.objects.get(name="TestCategory")
        self.product = Product.objects.get(name="MyProduct")
        self.user = User.objects.create_user(username='testuser', password='12345')

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
