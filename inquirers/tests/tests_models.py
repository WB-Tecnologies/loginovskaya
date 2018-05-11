from unittest import TestCase

from inquirers.models import FormEntity, FieldEntity, ChoiceScore


class FormEntityTestCase(TestCase):

    def test_str_method_return_title(self):
        """ Check that __str__ method return title """
        form_entity = FormEntity(title='Test form')
        self.assertEqual(str(form_entity), form_entity.title)


class FieldEntityTestCase(TestCase):

    def test_str_method_return_label(self):
        """ Check that __str__ method return label """
        field_entity = FieldEntity(label='Test field')
        self.assertEqual(str(field_entity), field_entity.label)


class ChoiceScoreTestCase(TestCase):

    def test_str_method_return_title(self):
        """ Check that __str__ method return title """
        choice_score = ChoiceScore(name='Test choice name')
        self.assertEqual(str(choice_score), choice_score.name)

    def test_form_title_property(self):
        """ Check that form title property return title of form entity from field entity """
        form_entity = FormEntity.objects.create(title='Test form name')
        field_entity = FieldEntity.objects.create(form_entity=form_entity, label='Test field label')
        choice_score = ChoiceScore.objects.create(field_entity=field_entity, name='Test choice score')
        self.assertEqual(choice_score.form_title, form_entity.title)
