from django.urls import path

from inquirers.forms import FirstForm, SecondForm, ThirdForm
from inquirers.views import InquireWizardView


named_inquire_forms = (('1', FirstForm), ('2', SecondForm), ('3', ThirdForm))
inquire_wizard = InquireWizardView.as_view(
    form_list=named_inquire_forms, url_name='inquire-step', done_step_name='inquire-result')

urlpatterns = [
    path('<step>', inquire_wizard, name='inquire-step'),
    path('result', inquire_wizard, name='inquire-result'),
]
