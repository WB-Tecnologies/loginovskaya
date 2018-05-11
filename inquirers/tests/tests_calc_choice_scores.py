from django import forms

from helpers.base_test import BaseTestCase
from inquirers.service import calc_choice_scores


class TestForm(forms.Form):

    TEST_RADIO1, TEST_RADIO2 = 'test-radio1', 'test-radio2'
    TEST_RADIO_FIELD_CHOICES = ((TEST_RADIO1, 'Test radio value 1'), (TEST_RADIO2, 'Test radio value 2'))
    TEST_CHECKBOX1, TEST_CHECKBOX2 = 'test-checkbox1', 'test-checkbox2'
    TEST_CHECKBOX_CHOICES = ((TEST_CHECKBOX1, 'Test checkbox value 1'), (TEST_CHECKBOX2, 'Test checkbox value 2'))

    test_radio_field = forms.ChoiceField(
        label='Test radio label', widget=forms.RadioSelect, choices=TEST_RADIO_FIELD_CHOICES, required=False)
    test_checkbox_field = forms.MultipleChoiceField(
        label='Test checkbox label', widget=forms.CheckboxSelectMultiple, choices=TEST_CHECKBOX_CHOICES,
        required=False)


class CalcChoiceScoresTestCase(BaseTestCase):

    def test_return_choice_score_cost_for_selected_radio_field(self):
        """ Check that return choice score cost for appropriate selected radio field """
        expected_cost, radio_field = 110, 'test_radio_field'
        form = TestForm(data={radio_field: TestForm.TEST_RADIO1})
        self.assertTrue(form.is_valid())
        form_entity = self.create_form_entity(form)
        field_entity = self.create_field_entity(form_entity=form_entity, name=radio_field)
        self.create_choice_score(field_entity=field_entity, value=form.TEST_RADIO1, cost=expected_cost)
        self.assertEqual(calc_choice_scores(form), expected_cost)

    def test_return_choice_score_cost_for_checked_checkbox_field(self):
        """ Check that return choice score cost for appropriate checked checkbox field """
        expected_cost, checkbox_field = 213, 'test_checkbox_field'
        form = TestForm(data={checkbox_field: [TestForm.TEST_CHECKBOX2]})
        self.assertTrue(form.is_valid())
        form_entity = self.create_form_entity(form)
        field_entity = self.create_field_entity(form_entity=form_entity, name=checkbox_field)
        self.create_choice_score(field_entity=field_entity, value=form.TEST_CHECKBOX2, cost=expected_cost)
        self.assertEqual(calc_choice_scores(form), expected_cost)

    def test_return_choice_score_cost_for_multiple_checked_checkbox_field(self):
        """ Check that return summary choice score cost for appropriate checked multiple checkbox options """
        cost1, cost2, checkbox_field = 400, 75, 'test_checkbox_field'
        expected_cost = cost1 + cost2
        form_data = {checkbox_field: [TestForm.TEST_CHECKBOX1, TestForm.TEST_CHECKBOX2]}
        form = TestForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_entity = self.create_form_entity(form)
        field_entity = self.create_field_entity(form_entity=form_entity, name=checkbox_field)
        self.create_choice_score(field_entity=field_entity, value=form.TEST_CHECKBOX1, cost=cost1)
        self.create_choice_score(field_entity=field_entity, value=form.TEST_CHECKBOX2, cost=cost2)
        self.assertEqual(calc_choice_scores(form), expected_cost)

    def test_return_summary_choice_score_cost_for_many_forms(self):
        """ Check that return summary choice score cost if set many forms """
        cost, radio_field = 110, 'test_radio_field'
        expected_cost = cost * 2
        form = TestForm(data={radio_field: TestForm.TEST_RADIO1})
        self.assertTrue(form.is_valid())
        form_entity = self.create_form_entity(form)
        field_entity = self.create_field_entity(form_entity=form_entity, name=radio_field)
        self.create_choice_score(field_entity=field_entity, value=form.TEST_RADIO1, cost=cost)
        self.assertEqual(calc_choice_scores(form, form), expected_cost)
