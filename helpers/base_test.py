from bs4 import BeautifulSoup
from django.test import TestCase
from django.test.client import Client


class BeautifulClient(Client):

    def request(self, **request):
        """ Return response with .get_html method """
        response = super().request(**request)
        try:
            response.get_html = lambda: BeautifulSoup(response.content, 'html.parser')
        except:
            response.get_html = lambda: None
        return response



class BaseTestCase(TestCase):

    client_class = BeautifulClient
