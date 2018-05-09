from formtools.wizard.views import NamedUrlSessionWizardView


class InquireWizardView(NamedUrlSessionWizardView):

    template_name = 'inquirers/step.html'

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form, **kwargs)
        context['form_template_name'] = 'inquirers/{}.html'.format(context['wizard']['steps'].current)
        return context
