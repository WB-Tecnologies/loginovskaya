from unittest import TestCase

from inquirers.forms import FirstForm


class FirstFormTestCase(TestCase):

    def test_count_errors_required_field(self):
        """ Check that count errors required field equal 5 if sent empty data """
        form = FirstForm(data=dict())
        form.is_valid()
        self.assertEqual(len(form.errors), 5)

    def test_valid_form_if_sent_data_for_all_fields(self):
        """ Check that form is valid if sent correct data for all fields """
        form = FirstForm(data=self._get_form_data())
        self.assertTrue(form.is_valid())

    def _get_form_data(self, **kwargs):
        form_data = dict(
            socials=['facebook'], events='needed', periodicity='everyday', subjects='ordinary', design='self')
        form_data.update(kwargs)
        return form_data
