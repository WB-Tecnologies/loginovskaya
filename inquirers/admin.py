from django.contrib import admin

from inquirers.models import ChoiceScore


class ChoiceScoreAdmin(admin.ModelAdmin):

    list_display = ('form_title', 'field_entity', 'name', 'cost')
    list_display_links = ('name', )
    list_filter = ('field_entity', )
    list_editable = ('cost', )
    fields = ('form_title', 'field_entity', 'name', 'cost')
    readonly_fields = ('form_title', 'field_entity', 'name')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions.pop('delete_selected', None)
        return actions


admin.site.register(ChoiceScore, ChoiceScoreAdmin)
