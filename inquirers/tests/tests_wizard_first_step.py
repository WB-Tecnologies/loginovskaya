from django.templatetags.static import static
from django.urls import reverse

from helpers.base_test import WizardStepTestCase
from inquirers.forms import FirstForm


class WizardFirstStepTestCase(WizardStepTestCase):

    URL_NAME = 'inquire-step'
    STEP = 1

    def test_resolve_url(self):
        """ Check that correct resolve url """
        self.assertEqual(self.URL, '/inquire/1')

    def test_redirect_to_second_step_url_after_post_valid_data(self):
        """ Check redirect to second step url after post valid data """
        response = self.client.post(self.URL, data=self._get_post_data())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse(self.URL_NAME, kwargs=dict(step=self.STEP+1)))

    def test_exist_socials_field(self):
        """ Check that exist socials field with correct attributes """
        socials_choices = FirstForm.SOCIALS_CHOICES
        response = self.client.get(self.URL)
        socials_checkboxes = response.get_html().find_all('input', attrs=dict(name=self._get_field_name('socials')))
        self.assertEqual(len(socials_checkboxes), len(socials_choices))
        for i, choice in enumerate(socials_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(socials_checkboxes[i]['value'], value)
                self.assertEqual(socials_checkboxes[i]['type'], 'checkbox')
                self.assertFalse(socials_checkboxes[i].has_attr('checked'))

    def test_display_checked_socials_checkboxes_for_errors_form(self):
        """ Check that display checked socials checkboxes for errors form """
        field_name = self._get_field_name('socials')
        for value, _ in FirstForm.SOCIALS_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: [value]}))
                socials_checkboxes = response.get_html().find_all(attrs=dict(name=self._get_field_name('socials')))
                socials_checked = [checkbox for checkbox in socials_checkboxes if checkbox.has_attr('checked')]
                self.assertEqual(len(socials_checked), 1)
                self.assertEqual(socials_checked[0]['value'], value)

    def test_exist_events_field(self):
        """ Check that exist events field with correct attributes """
        events_choices = FirstForm.EVENTS_CHOICES
        response = self.client.get(self.URL)
        events_radio = response.get_html().find_all('input', attrs=dict(name=self._get_field_name('events')))
        self.assertEqual(len(events_radio), len(events_choices))
        for i, choice in enumerate(events_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(events_radio[i]['value'], value)
                self.assertEqual(events_radio[i]['type'], 'radio')
                self.assertFalse(events_radio[i].has_attr('checked'))

    def test_display_checked_events_radio_for_errors_form(self):
        """ Check that display checked events radio for errors form """
        field_name = self._get_field_name('events')
        for value, _ in FirstForm.EVENTS_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                events_radio = response.get_html().find_all(attrs=dict(name=self._get_field_name('events')))
                events_checked = [radio for radio in events_radio if radio.has_attr('checked')]
                self.assertEqual(len(events_checked), 1)
                self.assertEqual(events_checked[0]['value'], value)

    def test_exist_periodicity_field(self):
        """ Check that exist periodicity with correct attributes """
        periodicity_choices = FirstForm.PERIODICITY_CHOICES
        response = self.client.get(self.URL)
        periodicity_radio = response.get_html().find_all(
            'input', attrs=dict(name=self._get_field_name('periodicity')))
        self.assertEqual(len(periodicity_radio), len(periodicity_choices))
        for i, choice in enumerate(periodicity_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(periodicity_radio[i]['value'], value)
                self.assertEqual(periodicity_radio[i]['type'], 'radio')
                self.assertFalse(periodicity_radio[i].has_attr('checked'))

    def test_display_checked_periodicity_radio_for_errors_form(self):
        """ Check that display checked periodicity radio for errors form """
        field_name = self._get_field_name('periodicity')
        for value, _ in FirstForm.PERIODICITY_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                periodicity_radio = response.get_html().find_all(attrs=dict(name=self._get_field_name('periodicity')))
                periodicity_checked = [radio for radio in periodicity_radio if radio.has_attr('checked')]
                self.assertEqual(len(periodicity_checked), 1)
                self.assertEqual(periodicity_checked[0]['value'], value)

    def test_exist_subjects_field(self):
        """ Check that exist subjects with correct attributes """
        subjects_choices = FirstForm.SUBJECTS_CHOICES
        response = self.client.get(self.URL)
        subjects_radio = response.get_html().find_all(
            'input', attrs=dict(name=self._get_field_name('subjects')))
        self.assertEqual(len(subjects_radio), len(subjects_choices))
        for i, choice in enumerate(subjects_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(subjects_radio[i]['value'], value)
                self.assertEqual(subjects_radio[i]['type'], 'radio')
                self.assertFalse(subjects_radio[i].has_attr('checked'))

    def test_display_checked_subjects_radio_for_errors_form(self):
        """ Check that display checked subjects radio for errors form """
        field_name = self._get_field_name('subjects')
        for value, _ in FirstForm.SUBJECTS_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                subjects_radio = response.get_html().find_all(attrs=dict(name=self._get_field_name('subjects')))
                subjects_checked = [radio for radio in subjects_radio if radio.has_attr('checked')]
                self.assertEqual(len(subjects_checked), 1)
                self.assertEqual(subjects_checked[0]['value'], value)

    def test_exist_design_field(self):
        """ Check that exist design with correct attributes """
        design_choices = FirstForm.DESIGN_CHOICES
        response = self.client.get(self.URL)
        design_radio = response.get_html().find_all(
            'input', attrs=dict(name=self._get_field_name('design')))
        self.assertEqual(len(design_radio), len(design_choices))
        for i, choice in enumerate(design_choices):
            value, label = choice
            with self.subTest(value=value):
                self.assertEqual(design_radio[i]['value'], value)
                self.assertEqual(design_radio[i]['type'], 'radio')
                self.assertFalse(design_radio[i].has_attr('checked'))

    def test_display_checked_design_radio_for_errors_form(self):
        """ Check that display checked design radio for errors form """
        field_name = self._get_field_name('design')
        for value, _ in FirstForm.DESIGN_CHOICES:
            with self.subTest(value=value):
                response = self.client.post(self.URL, data=self._get_only_data(**{field_name: value}))
                design_radio = response.get_html().find_all(attrs=dict(name=self._get_field_name('design')))
                design_checked = [radio for radio in design_radio if radio.has_attr('checked')]
                self.assertEqual(len(design_checked), 1)
                self.assertEqual(design_checked[0]['value'], value)

    def test_missing_button_previous(self):
        """ Check that missing button to previous step """
        response = self.client.get(self.URL)
        self.assertFalse(response.get_html().find(class_='c-step-previous'))

    def test_correct_socials_icons(self):
        """ Check that display correct socials icons """
        socials_choices = FirstForm.SOCIALS_CHOICES
        response = self.client.get(self.URL)
        socials_icons = response.get_html().find_all('img', class_='btn-socials')
        self.assertEqual(len(socials_icons), len(socials_choices))
        for i, choice in enumerate(socials_choices):
            value, label = choice
            with self.subTest(label=label):
                self.assertEqual(socials_icons[i]['src'], static('img/{}.svg'.format(value)))
                self.assertEqual(socials_icons[i]['alt'], label)

    def test_attribute_data_value_in_socials_links_as_socials_checkbox_value(self):
        """ Check that attribute data-value in socials links as socials checkbox value """
        socials_choices = FirstForm.SOCIALS_CHOICES
        response = self.client.get(self.URL)
        socials_links = response.get_html().find_all('a', class_='c-socials-link')
        self.assertEqual(len(socials_links), len(socials_choices))
        for i, choice in enumerate(socials_choices):
            value, _ = choice
            with self.subTest(value=value):
                self.assertEqual(socials_links[i]['data-value'], value)

    def test_socials_icons_marked_as_active_if_checked(self):
        """ Check that socials icons has active css class if checked """
        field_name = self._get_field_name('socials')
        checked_values = ['vkontakte', 'instagram']
        response = self.client.post(self.URL, data=self._get_only_data(**{field_name: checked_values}))
        self.assertEqual(response.status_code, 200)
        icons_active = response.get_html().find_all('img', class_='btn-active')
        self.assertEqual(len(icons_active), len(checked_values))
        for i, value in enumerate(checked_values):
            label = dict(FirstForm.SOCIALS_CHOICES)[value]
            with self.subTest(value=value):
                self.assertEqual(icons_active[i]['alt'], label)

    def _get_base_post_data(self):
        return dict(socials=['facebook'], events='needed', periodicity='everyday', subjects='ordinary', design='self')
