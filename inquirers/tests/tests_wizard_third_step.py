from django.templatetags.static import static
from django.urls import reverse

from helpers.base_test import WizardStepTestCase
from inquirers.forms import ThirdForm


class WizardThirdStepTestCase(WizardStepTestCase):

    STEP = 3

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
        self.assertEqual(response.url, reverse(self.URL_NAME, kwargs=dict(step=self.STEP+1)))

    def test_exist_tuning_field(self):
        """ Check that exist tuning field with correct attributes """
        tuning_choices = ThirdForm.TUNING_CHOICES
        response = self.client.get(self.URL)
        tuning_checkboxes = response.get_html().find_all('input', attrs=dict(name=self._get_field_name('tuning')))
        self.assertEqual(len(tuning_checkboxes), len(tuning_choices))
        for i, choice in enumerate(tuning_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(tuning_checkboxes[i]['value'], value)
                self.assertEqual(tuning_checkboxes[i]['type'], 'checkbox')
                self.assertFalse(tuning_checkboxes[i].has_attr('checked'))

    def test_display_checked_tuning_checkboxes_for_errors_form(self):
        """ Check that display checked tuning checkboxes for errors form """
        field_name = self._get_field_name('tuning')
        for value, _ in ThirdForm.TUNING_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: [value]}))
                tuning_checkboxes = response.get_html().find_all(attrs=dict(name=self._get_field_name('tuning')))
                tuning_checked = [checkbox for checkbox in tuning_checkboxes if checkbox.has_attr('checked')]
                self.assertEqual(len(tuning_checked), 1)
                self.assertEqual(tuning_checked[0]['value'], value)

    def test_exist_budget_field(self):
        """ Check that exist budget with correct attributes """
        budget_choices = ThirdForm.BUDGET_CHOICES
        response = self.client.get(self.URL)
        budget_radio = response.get_html().find_all('input', attrs=dict(name=self._get_field_name('budget')))
        self.assertEqual(len(budget_radio), len(budget_choices))
        for i, choice in enumerate(budget_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(budget_radio[i]['value'], value)
                self.assertEqual(budget_radio[i]['type'], 'radio')
                self.assertFalse(budget_radio[i].has_attr('checked'))

    def test_display_checked_budget_radio_for_errors_form(self):
        """ Check that display checked budget radio for errors form """
        field_name = self._get_field_name('budget')
        for value, _ in ThirdForm.BUDGET_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                budget_radio = response.get_html().find_all(attrs=dict(name=self._get_field_name('budget')))
                budget_checked = [radio for radio in budget_radio if radio.has_attr('checked')]
                self.assertEqual(len(budget_checked), 1)
                self.assertEqual(budget_checked[0]['value'], value)

    def test_exist_work_bloggers_field(self):
        """ Check that exist work_bloggers with correct attributes """
        work_bloggers_choices = ThirdForm.WORK_BLOGGERS_CHOICES
        response = self.client.get(self.URL)
        work_bloggers_radio = response.get_html().find_all(
            'input', attrs=dict(name=self._get_field_name('work_bloggers')))
        self.assertEqual(len(work_bloggers_radio), len(work_bloggers_choices))
        for i, choice in enumerate(work_bloggers_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(work_bloggers_radio[i]['value'], value)
                self.assertEqual(work_bloggers_radio[i]['type'], 'radio')
                self.assertFalse(work_bloggers_radio[i].has_attr('checked'))

    def test_display_checked_work_bloggers_radio_for_errors_form(self):
        """ Check that display checked work_bloggers radio for errors form """
        field_name = self._get_field_name('work_bloggers')
        for value, _ in ThirdForm.WORK_BLOGGERS_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                work_bloggers_radio = response.get_html().find_all(
                    attrs=dict(name=self._get_field_name('work_bloggers')))
                work_bloggers_checked = [radio for radio in work_bloggers_radio if radio.has_attr('checked')]
                self.assertEqual(len(work_bloggers_checked), 1)
                self.assertEqual(work_bloggers_checked[0]['value'], value)

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
        return dict(tuning=['third-party_sites'], budget='less100k', work_bloggers='more5')
