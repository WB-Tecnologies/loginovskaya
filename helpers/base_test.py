from bs4 import BeautifulSoup
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse_lazy

from inquirers.models import FormEntity, FieldEntity, ChoiceScore


class BeautifulClient(Client):

    def request(self, **request):
        """ Return response with .get_html method """
        response = super().request(**request)
        try:
            response.get_html = lambda: BeautifulSoup(response.content, 'html.parser')
        except Exception:
            response.get_html = lambda: None
        response.get_content = lambda: response.content.decode('utf-8')
        return response


class BaseTestCase(TestCase):

    client_class = BeautifulClient

    def create_form_entity(self, form=None, **kwargs):
        params = dict(title='Test form name', class_name='TestRadioForm')
        if form is not None:
            params['class_name'] = form.__class__.__name__
        params.update(kwargs)
        return FormEntity.objects.create(**params)

    def create_field_entity(self, **kwargs):
        params = dict(label='Test field label', name='test_field_name')
        if 'form_entity' not in kwargs:
            params['form_entity'] = self.create_form_entity()
        params.update(kwargs)
        return FieldEntity.objects.create(**params)

    def create_choice_score(self, **kwargs):
        params = dict(name='Test choice name', value='test-choice-value', cost=100)
        if 'field_entity' not in kwargs:
            params['field_entity'] = self.create_field_entity()
        params.update(kwargs)
        return ChoiceScore.objects.create(**params)


class WizardStepTestCase(BaseTestCase):

    URL_NAME = 'inquire-step'
    STEP = 1
    SESSION_PREFIX_KEY = 'wizard_inquire_wizard_view'

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

    def _setup_session(self, step=None):
        session = self.client.session
        session[self.SESSION_PREFIX_KEY] = dict(step=(step or self.STEP), step_data={}, step_files={}, extra_data={})
        session.save()
