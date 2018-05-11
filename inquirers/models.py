from django.db import models


class FormEntity(models.Model):

    title = models.CharField('Название формы', max_length=200)
    class_name = models.CharField('Название класса формы', max_length=200, unique=True, editable=False)

    class Meta:
        verbose_name = 'Форма опросника'
        verbose_name_plural = 'Формы опросника'
        ordering = ('title', )

    def __str__(self):
        return self.title


class FieldEntity(models.Model):

    form_entity = models.ForeignKey(FormEntity, verbose_name='Форма опросника', on_delete=models.CASCADE)
    label = models.CharField('Заголовок поля', max_length=200)
    name = models.CharField('Название поля', max_length=200, editable=False)

    class Meta:
        verbose_name = 'Поле опросника'
        verbose_name_plural = 'Поля опросника'
        ordering = ('label', )
        unique_together = (('form_entity', 'name'), )

    def __str__(self):
        return self.label


class ChoiceScore(models.Model):

    field_entity = models.ForeignKey(FieldEntity, verbose_name='Поле опросника', on_delete=models.CASCADE)
    name = models.CharField('Название опции', max_length=200)
    value = models.CharField('Значение опции', max_length=200, editable=False)
    cost = models.PositiveIntegerField('Стоимость опции', default=0, help_text='указывается в рублях')

    class Meta:
        verbose_name = 'Значение для подсчета'
        verbose_name_plural = 'Значения для подсчета'
        ordering = ('name', )
        unique_together = (('field_entity', 'value'), )

    def __str__(self):
        return self.name

    @property
    def form_title(self):
        return self.field_entity.form_entity.title
    form_title.fget.short_description = 'Форма'
