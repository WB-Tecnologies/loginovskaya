from django.shortcuts import render
from formtools.wizard.views import NamedUrlSessionWizardView

from inquirers.service import calc_choice_scores


class InquireWizardView(NamedUrlSessionWizardView):

    template_name = 'inquirers/step.html'

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form, **kwargs)
        context['form_template_name'] = 'inquirers/{}.html'.format(context['wizard']['steps'].current)
        return context

    def done(self, form_list, **kwargs):
        context = dict(total_cost=calc_choice_scores(*form_list))
        return render(self.request, 'inquirers/result.html', context=context)
