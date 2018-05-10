from django.templatetags.static import static
from django.urls import reverse_lazy

from helpers.base_test import WizardStepTestCase


class WizardResultTestCase(WizardStepTestCase):

    URL = reverse_lazy(WizardStepTestCase.URL_NAME, kwargs=dict(step='result'))

    def setUp(self):
        session = self.client.session
        session[self.SESSION_PREFIX_KEY] = {
            'step': '4', 'step_data': {
                '1': {'inquire_wizard_view-current_step': ['1'], '1-socials': ['twitter', 'odnoklassniki'],
                      '1-events': ['not-needed'], '1-periodicity': ['twiceday'], '1-subjects': ['ordinary'],
                      '1-design': ['prepare']},
                '2': {'inquire_wizard_view-current_step': ['2'], '2-negotiation': ['no'], '2-monitoring': ['weekly'],
                      '2-matrix_answers': ['no']},
                '3': {'inquire_wizard_view-current_step': ['3'], '3-tuning': ['targeting_fb+insta'],
                      '3-budget': ['more100k'], '3-work_bloggers': ['more5']},
                '4': {'inquire_wizard_view-current_step': ['4'], '4-regions': ['moscow'], '4-executor': ['more100k'],
                      '4-agreement_chain': ['more2']}},
            'step_files': {'1': {}, '2': {}, '3': {}, '4': {}},
            'extra_data': {}}
        session.save()

    def test_resolve_url(self):
        """ Check that correct resolve url """
        self.assertEqual(self.URL, '/inquire/result')

    def test_title_contains_final(self):
        """ Check that title contains `Final` """
        response = self.client.get(self.URL, follow=True)
        title = response.get_html().find('title')
        self.assertIn('Final', title.get_text())

    def test_missing_button_previous(self):
        """ Check that missing button to previous step """
        response = self.client.get(self.URL)
        self.assertFalse(response.get_html().find(class_='c-step-previous'))

    def test_correct_display_steps_image(self):
        """ Check that correct display steps image """
        response = self.client.get(self.URL)
        steps_image = response.get_html().find('img', class_='stepsStyle')
        self.assertEqual(steps_image['src'], static('img/steps-5.svg'))
