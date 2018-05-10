from django.templatetags.static import static
from django.urls import reverse

from helpers.base_test import WizardStepTestCase
from inquirers.forms import SecondForm


class WizardSecondStepTestCase(WizardStepTestCase):

    STEP = 2
    SESSION_PREFIX_KEY = 'wizard_inquire_wizard_view'

    def setUp(self):
        super().setUp()
        session = self.client.session
        session[self.SESSION_PREFIX_KEY] = dict(step=self.STEP, step_data={}, step_files={}, extra_data={})
        session.save()

    def test_resolve_url(self):
        """ Check that correct resolve url """
        self.assertEqual(self.URL, '/inquire/2')

    def test_title_contains_number_step(self):
        """ Check that title contains '2st step' """
        response = self.client.get(self.URL)
        title = response.get_html().find('title')
        self.assertIn('2st step', title.get_text())

    def test_redirect_to_third_step_url_after_post_valid_data(self):
        """ Check redirect to third step url after post valid data """
        response = self.client.post(self.URL, data=self._get_post_data())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse(self.URL_NAME, kwargs=dict(step=self.STEP+1)))

    def test_exist_negotiation_field(self):
        """ Check that exist negotiation field with correct attributes """
        negotiation_choices = SecondForm.NEGOTIATION_CHOICES
        response = self.client.get(self.URL)
        negotiation_radio = response.get_html().find_all('input', attrs=dict(name=self._get_field_name('negotiation')))
        self.assertEqual(len(negotiation_radio), len(negotiation_choices))
        for i, choice in enumerate(negotiation_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(negotiation_radio[i]['value'], value)
                self.assertEqual(negotiation_radio[i]['type'], 'radio')
                self.assertFalse(negotiation_radio[i].has_attr('checked'))

    def test_display_checked_negotiation_radio_for_errors_form(self):
        """ Check that display checked negotiation radio for errors form """
        field_name = self._get_field_name('negotiation')
        for value, _ in SecondForm.NEGOTIATION_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                negotiation_radio = response.get_html().find_all(attrs=dict(name=self._get_field_name('negotiation')))
                negotiation_checked = [radio for radio in negotiation_radio if radio.has_attr('checked')]
                self.assertEqual(len(negotiation_checked), 1)
                self.assertEqual(negotiation_checked[0]['value'], value)

    def test_exist_monitoring_field(self):
        """ Check that exist monitoring with correct attributes """
        monitoring_choices = SecondForm.MONITORING_CHOICES
        response = self.client.get(self.URL)
        monitoring_radio = response.get_html().find_all(
            'input', attrs=dict(name=self._get_field_name('monitoring')))
        self.assertEqual(len(monitoring_radio), len(monitoring_choices))
        for i, choice in enumerate(monitoring_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(monitoring_radio[i]['value'], value)
                self.assertEqual(monitoring_radio[i]['type'], 'radio')
                self.assertFalse(monitoring_radio[i].has_attr('checked'))

    def test_display_checked_monitoring_radio_for_errors_form(self):
        """ Check that display checked monitoring radio for errors form """
        field_name = self._get_field_name('monitoring')
        for value, _ in SecondForm.MONITORING_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                monitoring_radio = response.get_html().find_all(attrs=dict(name=self._get_field_name('monitoring')))
                monitoring_checked = [radio for radio in monitoring_radio if radio.has_attr('checked')]
                self.assertEqual(len(monitoring_checked), 1)
                self.assertEqual(monitoring_checked[0]['value'], value)

    def test_exist_matrix_answers_field(self):
        """ Check that exist matrix_answers with correct attributes """
        matrix_answers_choices = SecondForm.MATRIX_ANSWERS_CHOICES
        response = self.client.get(self.URL)
        matrix_answers_radio = response.get_html().find_all(
            'input', attrs=dict(name=self._get_field_name('matrix_answers')))
        self.assertEqual(len(matrix_answers_radio), len(matrix_answers_choices))
        for i, choice in enumerate(matrix_answers_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(matrix_answers_radio[i]['value'], value)
                self.assertEqual(matrix_answers_radio[i]['type'], 'radio')
                self.assertFalse(matrix_answers_radio[i].has_attr('checked'))

    def test_display_checked_matrix_answers_radio_for_errors_form(self):
        """ Check that display checked matrix_answers radio for errors form """
        field_name = self._get_field_name('matrix_answers')
        for value, _ in SecondForm.MATRIX_ANSWERS_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                matrix_answers_radio = response.get_html().find_all(attrs=dict(name=self._get_field_name('matrix_answers')))
                matrix_answers_checked = [radio for radio in matrix_answers_radio if radio.has_attr('checked')]
                self.assertEqual(len(matrix_answers_checked), 1)
                self.assertEqual(matrix_answers_checked[0]['value'], value)

    def test_display_button_previous_with_correct_attribute_data_url(self):
        """ Check that display button to previous step with data-url as previous step url """
        response = self.client.get(self.URL)
        previous_button = response.get_html().find(class_='c-step-previous')
        self.assertTrue(previous_button)
        self.assertEqual(previous_button['data-url'], reverse('inquire-step', kwargs=dict(step=self.STEP-1)))

    def test_correct_display_steps_image(self):
        """ Check that correct display steps image """
        response = self.client.get(self.URL)
        steps_image = response.get_html().find('img', class_='stepsStyle')
        self.assertEqual(steps_image['src'], static('img/steps-{}.svg'.format(self.STEP)))

    def _get_base_post_data(self):
        return dict(negotiation='no', monitoring='monthly', matrix_answers='yes')
