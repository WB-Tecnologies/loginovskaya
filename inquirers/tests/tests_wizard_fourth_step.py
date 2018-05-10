from django.templatetags.static import static
from django.urls import reverse

from helpers.base_test import WizardStepTestCase
from inquirers.forms import FourthForm


class WizardFourthStepTestCase(WizardStepTestCase):

    STEP = 4

    def setUp(self):
        super().setUp()
        self._setup_session()

    def test_resolve_url(self):
        """ Check that correct resolve url """
        self.assertEqual(self.URL, '/inquire/{}'.format(self.STEP))

    def test_title_contains_number_step(self):
        """ Check that title contains step number """
        response = self.client.get(self.URL)
        title = response.get_html().find('title')
        self.assertIn('{}st step'.format(self.STEP), title.get_text())

    def test_redirect_to_third_step_url_after_post_valid_data(self):
        """ Check redirect to third step url after post valid data """
        response = self.client.post(self.URL, data=self._get_post_data())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('inquire-result'))

    def test_exist_regions_field(self):
        """ Check that exist regions field with correct attributes """
        regions_choices = FourthForm.REGIONS_CHOICES
        response = self.client.get(self.URL)
        regions_checkboxes = response.get_html().find_all('input', attrs=dict(name=self._get_field_name('regions')))
        self.assertEqual(len(regions_checkboxes), len(regions_choices))
        for i, choice in enumerate(regions_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(regions_checkboxes[i]['value'], value)
                self.assertEqual(regions_checkboxes[i]['type'], 'checkbox')
                self.assertFalse(regions_checkboxes[i].has_attr('checked'))

    def test_display_checked_regions_checkboxes_for_errors_form(self):
        """ Check that display checked regions checkboxes for errors form """
        field_name = self._get_field_name('regions')
        for value, _ in FourthForm.REGIONS_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: [value]}))
                regions_checkboxes = response.get_html().find_all(attrs=dict(name=self._get_field_name('regions')))
                regions_checked = [checkbox for checkbox in regions_checkboxes if checkbox.has_attr('checked')]
                self.assertEqual(len(regions_checked), 1)
                self.assertEqual(regions_checked[0]['value'], value)

    def test_exist_executor_field(self):
        """ Check that exist executor with correct attributes """
        executor_choices = FourthForm.EXECUTOR_CHOICES
        response = self.client.get(self.URL)
        executor_radio = response.get_html().find_all('input', attrs=dict(name=self._get_field_name('executor')))
        self.assertEqual(len(executor_radio), len(executor_choices))
        for i, choice in enumerate(executor_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(executor_radio[i]['value'], value)
                self.assertEqual(executor_radio[i]['type'], 'radio')
                self.assertFalse(executor_radio[i].has_attr('checked'))

    def test_display_checked_executor_radio_for_errors_form(self):
        """ Check that display checked executor radio for errors form """
        field_name = self._get_field_name('executor')
        for value, _ in FourthForm.EXECUTOR_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                executor_radio = response.get_html().find_all(attrs=dict(name=self._get_field_name('executor')))
                executor_checked = [radio for radio in executor_radio if radio.has_attr('checked')]
                self.assertEqual(len(executor_checked), 1)
                self.assertEqual(executor_checked[0]['value'], value)

    def test_exist_agreement_chain_field(self):
        """ Check that exist agreement_chain with correct attributes """
        agreement_chain_choices = FourthForm.AGREEMENT_CHAIN_CHOICES
        response = self.client.get(self.URL)
        agreement_chain_radio = response.get_html().find_all(
            'input', attrs=dict(name=self._get_field_name('agreement_chain')))
        self.assertEqual(len(agreement_chain_radio), len(agreement_chain_choices))
        for i, choice in enumerate(agreement_chain_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(agreement_chain_radio[i]['value'], value)
                self.assertEqual(agreement_chain_radio[i]['type'], 'radio')
                self.assertFalse(agreement_chain_radio[i].has_attr('checked'))

    def test_display_checked_agreement_chain_radio_for_errors_form(self):
        """ Check that display checked agreement_chain radio for errors form """
        field_name = self._get_field_name('agreement_chain')
        for value, _ in FourthForm.AGREEMENT_CHAIN_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                agreement_chain_radio = response.get_html().find_all(
                    attrs=dict(name=self._get_field_name('agreement_chain')))
                agreement_chain_checked = [radio for radio in agreement_chain_radio if radio.has_attr('checked')]
                self.assertEqual(len(agreement_chain_checked), 1)
                self.assertEqual(agreement_chain_checked[0]['value'], value)

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
        return dict(regions=['other'], executor='less100k', agreement_chain='more2')
