from collections import defaultdict

from inquirers.models import ChoiceScore


def calc_choice_scores(*valid_forms):
    all_costs = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for obj in ChoiceScore.objects.all().select_related('field_entity', 'field_entity__form_entity'):
        all_costs[obj.field_entity.form_entity.class_name][obj.field_entity.name][obj.value] = obj.cost
    total_cost = 0
    for form in valid_forms:
        for field_name, values in form.cleaned_data.items():
            if not isinstance(values, list):
                values = [values]
            for value in values:
                total_cost += all_costs[form.__class__.__name__][field_name][value]
    return total_cost
