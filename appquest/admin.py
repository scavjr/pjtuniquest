from django import forms
from django.contrib import admin

# Register your models here.
from .models import Questions, AltQuestion, Curso, Assunto


class CursoAdmin(admin.ModelAdmin):

    list_display = ('cursonome', 'eixonome')
    
    
class AssuntoAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'assuntonome', 'cursoid')

class QuestionsAdminForm(forms.ModelForm):

    class Meta:
        model = Questions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(QuestionsAdminForm, self).__init__(*args, **kwargs)
        rsp_ids = Questions.objects.filter(qtext=self.instance)[:1]
        self.fields['rspcorretaid'].queryset = AltQuestion.objects.filter(qid_id=rsp_ids).order_by('alttexto')


class QuestionsAdmin(admin.ModelAdmin):

    form = QuestionsAdminForm
    readonly_fields = ('id',)
    list_display = ('qtext', 'qimagem','cursoid','assuntoid', 'semana','tipoquestao')

   
    
class AltQuestionAdmin(admin.ModelAdmin):
    
    
     list_display = ('alttexto', 'altcorreta', 'altjustif', 'qid')


admin.site.register(Curso, CursoAdmin)
admin.site.register(Assunto, AssuntoAdmin)
admin.site.register(AltQuestion, AltQuestionAdmin)
admin.site.register(Questions, QuestionsAdmin)



