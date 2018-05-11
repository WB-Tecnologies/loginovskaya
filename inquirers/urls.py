from django.urls import path

from inquirers.forms import FirstForm, SecondForm, ThirdForm, FourthForm
from inquirers.views import InquireWizardView


named_inquire_forms = (('1', FirstForm), ('2', SecondForm), ('3', ThirdForm), ('4', FourthForm))
inquire_wizard = InquireWizardView.as_view(
    form_list=named_inquire_forms, url_name='inquire-step', done_step_name='result')

urlpatterns = [
    path('inquire/<step>', inquire_wizard, name='inquire-step'),
    path('', inquire_wizard, name='home'),
]
