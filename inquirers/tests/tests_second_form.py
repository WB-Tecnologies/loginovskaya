from unittest import TestCase

from inquirers.forms import SecondForm


class SecondFormTestCase(TestCase):

    def test_count_errors_required_field(self):
        """ Check that count errors required field equal 3 if sent empty data """
        form = SecondForm(data=dict())
        form.is_valid()
        self.assertEqual(len(form.errors), 3)

    def test_valid_form_if_sent_data_for_all_fields(self):
        """ Check that form is valid if sent correct data for all fields """
        form = SecondForm(data=self._get_form_data())
        self.assertTrue(form.is_valid())

    def _get_form_data(self, **kwargs):
        form_data = dict(negotiation='yes', monitoring='weekly', matrix_answers='no')
        form_data.update(kwargs)
        return form_data
