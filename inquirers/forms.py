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


class ThirdForm(forms.Form):

    TUNING_CHOICES = (
        ('targeting_fb+insta', 'Настройка таргетинга в ФБ+Инста'),
        ('targeting_ok', 'Настройка таргетинга в ОК'),
        ('third-party_sites', 'Размещение рекламных постов на сторонних площадках'),
        ('targeting_vk', 'Настройка таргетинга в ВК'))
    BUDGET_CHOICES = (('less100k', 'До 100 000'), ('more100k', 'Более 100 000'))
    WORK_BLOGGERS_CHOICES = (('less5', 'До 5 в месяц'), ('more5', 'Более 5 в месяц'))
    tuning = forms.MultipleChoiceField(
        label='Настройка', widget=forms.CheckboxSelectMultiple, choices=TUNING_CHOICES)
    budget = forms.ChoiceField(label='Бюджет', widget=forms.RadioSelect, choices=BUDGET_CHOICES)
    work_bloggers = forms.ChoiceField(
        label='Работа с блогерами', widget=forms.RadioSelect, choices=WORK_BLOGGERS_CHOICES)


class FourthForm(forms.Form):

    REGIONS_CHOICES = (('moscow', 'Москва'), ('spb', 'Санкт-Петербург'), ('other', 'Другие регионы'))
    EXECUTOR_CHOICES = (('less100k', 'До 100 000'), ('more100k', 'Более 100 000'))
    AGREEMENT_CHAIN_CHOICES = (('one', '1 человек'), ('more2', '2 и более человек'))
    regions = forms.MultipleChoiceField(label='Регионы', widget=forms.CheckboxSelectMultiple, choices=REGIONS_CHOICES)
    executor = forms.ChoiceField(label='Агенство или фрилансер', widget=forms.RadioSelect, choices=EXECUTOR_CHOICES)
    agreement_chain = forms.ChoiceField(
        label='Цепочка согласования', widget=forms.RadioSelect, choices=AGREEMENT_CHAIN_CHOICES)
