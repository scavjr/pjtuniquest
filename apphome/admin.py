from django.contrib import admin

from apphome.models import ListQuestAtual


class ListQuestAtualAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'date_publication', 'descricao')


admin.site.register(ListQuestAtual, ListQuestAtualAdmin)