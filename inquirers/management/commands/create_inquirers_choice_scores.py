from django.core.management.base import BaseCommand

from inquirers.models import FormEntity, FieldEntity, ChoiceScore
from inquirers.urls import named_inquire_forms


class Command(BaseCommand):

    help = 'Create inquirers choices for set cost from admin'

    def handle(self, *args, **options):
        self.stdout.write('Start.')
        choice_exist_counter, choice_created_counter = 0, 0
        for step, form_cls in named_inquire_forms:
            self.stdout.write('Prepared form {}...'.format(form_cls.__name__))
            form_entity, _ = FormEntity.objects.get_or_create(
                class_name=form_cls.__name__, defaults=dict(title='Форма для шага №{}.'.format(step)))
            for name, field in form_cls().fields.items():
                field_entity, _ = FieldEntity.objects.get_or_create(
                    form_entity=form_entity, name=name, defaults=dict(label=field.label))
                if hasattr(field, 'choices'):
                    choice_exist_counter += len(field.choices)
                    for choice_value, choice_name in field.choices:
                        choice_score, choice_created = ChoiceScore.objects.get_or_create(
                            field_entity=field_entity, value=choice_value, defaults=dict(name=choice_name))
                        choice_created_counter += int(choice_created)
        self.stdout.write('Found field choices: {}'.format(choice_exist_counter))
        self.stdout.write('Created new choice score instances: {}'.format(choice_created_counter))
        self.stdout.write('End.')
