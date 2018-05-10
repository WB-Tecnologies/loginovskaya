from django import forms


class FirstForm(forms.Form):

    SOCIALS_CHOICES = (
        ('vkontakte', 'Vkontakte'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('youtube', 'Youtube'),
        ('instagram', 'Instagram'),
        ('odnoklassniki', 'Odnoklassniki'))
    EVENTS_CHOICES = (
        ('needed', 'Нужны'),
        ('not-needed', 'Не нужны'))
    PERIODICITY_CHOICES = (
        ('everyday', 'Каждый день'),
        ('twiceday', '2 раза в день'),
        ('threefourday', '3-4 раза в день'))
    SUBJECTS_CHOICES = (
        ('complicated', 'Сложная'),
        ('ordinary', 'Простая'))
    DESIGN_CHOICES = (
        ('self', 'Свои картинки'),
        ('buy', 'Покупать картинки'),
        ('prepare', 'Обрабатывать картинки'))
    socials = forms.MultipleChoiceField(
        label='Социальные сети', widget=forms.CheckboxSelectMultiple, choices=SOCIALS_CHOICES)
    events = forms.ChoiceField(label='Мероприятия', widget=forms.RadioSelect, choices=EVENTS_CHOICES)
    periodicity = forms.ChoiceField(label='Периодичность', widget=forms.RadioSelect, choices=PERIODICITY_CHOICES)
    subjects = forms.ChoiceField(label='Тематика', widget=forms.RadioSelect, choices=SUBJECTS_CHOICES)
    design = forms.ChoiceField(label='Дизайн', widget=forms.RadioSelect, choices=DESIGN_CHOICES)


class SecondForm(forms.Form):

    NEGOTIATION_CHOICES = (('yes', 'Да'), ('no', 'Нет'))
    MONITORING_CHOICES = (('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно'))
    MATRIX_ANSWERS_CHOICES = (('yes', 'Да'), ('no', 'Нет'))
    negotiation = forms.ChoiceField(
        label='Отработка негатива', widget=forms.RadioSelect, choices=NEGOTIATION_CHOICES)
    monitoring = forms.ChoiceField(label='Мониторинг', widget=forms.RadioSelect, choices=MONITORING_CHOICES)
    matrix_answers = forms.ChoiceField(
        label='Матрица ответов', widget=forms.RadioSelect, choices=MATRIX_ANSWERS_CHOICES)
