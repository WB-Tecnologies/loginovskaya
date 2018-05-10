from unittest import TestCase

from inquirers.forms import ThirdForm


class ThirdFormTestCase(TestCase):

    def test_count_errors_required_field(self):
        """ Check that count errors required field equal 3 if sent empty data """
        form = ThirdForm(data=dict())
        form.is_valid()
        self.assertEqual(len(form.errors), 3)

    def test_valid_form_if_sent_data_for_all_fields(self):
        """ Check that form is valid if sent correct data for all fields """
        form = ThirdForm(data=self._get_form_data())
        self.assertTrue(form.is_valid())

    def _get_form_data(self, **kwargs):
        form_data = dict(tuning=['targeting_vk'], budget='more100k', work_bloggers='less5')
        form_data.update(kwargs)
        return form_data
