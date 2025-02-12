from django.db import models


class ListQuestAtual(models.Model):
    date_publication = models.DateTimeField(auto_now=False, auto_now_add=True)
    descricao = models.CharField()

    list_display = ['date_publication', 'descricao']

    class Meta:
        ordering = ['-date_publication']

    def __str__(self):
        return self.descricao

