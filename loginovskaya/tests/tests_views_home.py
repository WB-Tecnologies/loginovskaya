from django.urls import reverse, reverse_lazy

from helpers.base_test import BaseTestCase


class HomeViewTestCase(BaseTestCase):

    URL_NAME = 'home'
    URL = reverse_lazy(URL_NAME)

    def test_resolve_url(self):
        """ Check that correct resolve url as '/' """
        self.assertEqual(self.URL, '/')

    def test_exist_first_step_link(self):
        """ Check that exist first step link """
        response = self.client.get(self.URL)
        self.assertIn(reverse('inquire-step', args=(1, )), response.get_content())
