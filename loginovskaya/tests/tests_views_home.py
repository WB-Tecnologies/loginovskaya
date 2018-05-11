from django.urls import reverse_lazy, reverse

from helpers.base_test import BaseTestCase


class HomeViewTestCase(BaseTestCase):

    URL_NAME = 'home'
    URL = reverse_lazy(URL_NAME)

    def test_resolve_url(self):
        """ Check that correct resolve url as '/' """
        self.assertEqual(self.URL, '/')

    def test_redirect_from_home_to_inquirer_first_step(self):
        """ Check that redirect from home to inquirer first step """
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('inquire-step', kwargs=dict(step=1)))
