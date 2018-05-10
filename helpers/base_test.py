from bs4 import BeautifulSoup
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse_lazy


class BeautifulClient(Client):

    def request(self, **request):
        """ Return response with .get_html method """
        response = super().request(**request)
        try:
            response.get_html = lambda: BeautifulSoup(response.content, 'html.parser')
        except:
            response.get_html = lambda: None
        response.get_content = lambda: response.content.decode('utf-8')
        return response


class BaseTestCase(TestCase):

    client_class = BeautifulClient


class WizardStepTestCase(BaseTestCase):

    URL_NAME = 'inquire-step'
    STEP = 1

    def setUp(self):
        super().setUp()
        self.URL = reverse_lazy(self.URL_NAME, kwargs=dict(step=self.STEP))
        self.MANAGEMENT_DATA = {'inquire_wizard_view-current_step': self.STEP}

    def _get_field_name(self, name):
        return '{}-{}'.format(self.STEP, name)

    def _get_base_post_data(self):
        return dict()

    def _get_post_data(self, **kwargs):
        post_data = {self._get_field_name(name): value for name, value in self._get_base_post_data().items()}
        post_data.update(self.MANAGEMENT_DATA)
        post_data.update(kwargs)
        return post_data

    def _get_only_data(self, **kwargs):
        post_data = dict()
        post_data.update(self.MANAGEMENT_DATA)
        post_data.update(kwargs)
        return post_data
