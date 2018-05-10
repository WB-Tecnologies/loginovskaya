from django.urls import path

from inquirers.forms import FirstForm, SecondForm
from inquirers.views import InquireWizardView


inquire_wizard = InquireWizardView.as_view(
    [('1', FirstForm), ('2', SecondForm)], url_name='inquire-step', done_step_name='inquire-result')


urlpatterns = [
    path('<step>', inquire_wizard, name='inquire-step'),
    path('result', inquire_wizard, name='inquire-result'),
]