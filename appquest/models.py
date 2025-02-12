from django.db import models
#clsfrom ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
TIPOQUESTAO_CHOICES = [
        (1, "AVA"),
        (2, "Texto Base"),
        (3, "Videoaulas"),
        (4, "Slides"),
        (5, "Outras"),
    ]

SEMANA_CHOICES = [
        (1, "Semana 1"),
        (2, "Semana 2"),
        (3, "Semana 3"),
        (4, "Semana 4"),
        (5, "Semana 5"),
        (6, "Semana 6"),
        (7, "Semana 7"),
    ]

EIXO_NOME_CHOICES = [
        ('COMP', "Eixo de Computação"),
        ('LIC', "Eixo de Licenciatura"),
        ('NEG', "Eixo de Negócio")
]


class Curso(models.Model):
    readonly_fields = ('id',)
    cursonome = models.CharField()
    eixonome = models.CharField(choices=EIXO_NOME_CHOICES)
        
    def __str__(self):
        return self.cursonome
    
class Assunto(models.Model):
    assuntonome = models.CharField()
    cursoid = models.ForeignKey('Curso', verbose_name="Curso", on_delete=models.CASCADE)


    
    def __str__(self):
        return self.assuntonome

class Questions(models.Model):

    qtext = RichTextUploadingField(blank=True, null=True)
    #qtext = models.TextField()
    qimagem = models.ImageField(upload_to='appquest', blank=True)
    cursoid = models.ForeignKey('Curso',verbose_name="Curso", on_delete=models.CASCADE,)
    assuntoid = models.ForeignKey('Assunto', on_delete=models.CASCADE,)
    rspcorretaid = models.ForeignKey('AltQuestion',verbose_name="AltQuestion", on_delete=models.CASCADE, )
    justresposta = models.CharField(blank=True)
    semana = models.IntegerField(choices=SEMANA_CHOICES,)
    tipoquestao = models.IntegerField(choices=TIPOQUESTAO_CHOICES,)

    def __str__(self):
        return self.qtext or ''


class AltQuestion(models.Model):
    alttexto = models.TextField()
    altcorreta = models.BooleanField()
    altjustif = models.TextField(blank=True)
    qid = models.ForeignKey('Questions', verbose_name="Questão", on_delete=models.CASCADE,)

    def __str__(self):
        return self.alttexto