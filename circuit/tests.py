from django.test import TestCase, Client
from django.urls import reverse

from circuit.models import InfoChain, Contact, Staff, Product

c = Client()


# Create your tests here.
class TestChain(TestCase):
    def setUp(self):
        contact = Contact.objects.create(
            email='test_email',
            country='test_country',
            city='test_city',
            street='test_street',
            number_house=1
        )
        product = Product.objects.create(
            title_product='test_product',
            model='test_model',
            date='2202-02-20 00:00'
        )
        staff = Staff.objects.create_user(
            username='test_username_1',
            password='test_password',
            is_active=True,
            first_name='test_first_name',
            last_name='test_last_name'
        )
        InfoChain.objects.create(
            title='title_test',
            structure='plant',
            staff=staff,
            supplier=None,
            products=product,
            contacts=contact,

        )

    def test_chain(self):

        staff = c.post(
            Staff.objects.create_user(
                username='test_username_2',
                password='test_password',
                is_active=True,
                first_name='test_first_name',
                last_name='test_last_name'
            ))
        auth = c.post(
            '/api-auth/login/',
            {
                'username': 'test_username_2',
                'password': 'test_password'
            }
        )
        list_chain = reverse('all_chain')
        list_chain = c.get(list_chain)
        self.assertNotContains(list_chain, status_code=200, text='staff is not is_active')
        country = c.get('/country/?contacts__country=test_country')
        self.assertNotContains(country, status_code=200, text='Неизвестная ошибка')








