from django.shortcuts import render
from apphome.views import obter_assunto, obter_cursos, obter_list_atual
from appquest.forms import QuestionForm
from appquest.models import Curso, Questions, AltQuestion
from django.db.models import F
from django.contrib.auth.decorators import login_required


def opcaotexto(argumento, nrquestaorespondidas):
    if argumento == 0:
        return "Você errou todas as questões de " + str(nrquestaorespondidas) + ". Reveja o assunto e tente novamente."
    elif argumento == 1:
        return "Você acertou uma questão de " + str(nrquestaorespondidas) + "."
    else:
        return "Você acertou " + str(argumento) + " questões de " + str(nrquestaorespondidas) + "."


@login_required
def verQuestao(request):
    print('qqq')
    assuntos = obter_assunto(request)
    cursos = obter_cursos(request)
    lista_atual = obter_list_atual()
    #sessao = request.session.get("logado")
    sessaonomecompleto = request.session.get("sessaonomecompleto")
    if ((request.method == 'GET')):
        print('req')
        paramslist = dict(request.GET.items())
        if len(paramslist) != 0:
            tipoquestao = paramslist['tipoquestao']
            curso = paramslist['curso']
            assunto = 'todos'  # paramslist['assunto']
            semana = paramslist['semana']
            cursoname = Curso.objects.filter(id=curso).values()[0]['cursonome']
            tituloquest = cursoname + " - semana " + semana
            form = QuestionForm
            todos = []
            dictodos = {}
            if assunto == "todos":
                parent = Questions.objects.filter(cursoid=curso).filter(semana=semana).filter(tipoquestao=tipoquestao)
            else:
                parent = Questions.objects.filter(cursoid=curso).filter(semana=semana).filter(tipoquestao=tipoquestao).filter(assuntoid=assunto)
            
            for j in parent:
                todos.append(j.altquestion_set.all().values)
                todos.append(j.qimagem)
                todos.append(j.id)
                dictodos[j.qtext] = todos
                todos = []
            ha_questao = len(dictodos)
            return render(request, 'appquest/appquest_question.html', {"form": form, "todos": dictodos, 'titulo': tituloquest, 'haquestao': ha_questao,  'usuario': sessaonomecompleto, 'assuntos': assuntos, 'cursos': cursos})
        else:
            return render(request, 'apphome/apphome_dashboard.html', {'usuario': sessaonomecompleto, 'assuntos': assuntos, 'cursos': cursos, 'lista_atual': lista_atual})
    else:
        rsplist = list(request.POST.values())
        rspcorretas = obter_rsp_corretas(rsplist[1:])
        return render(request, 'appquest/appquest_question.html', {'rspcorretas': rspcorretas[0], 'rsplist': list(rspcorretas[1]), 'textcorr': rspcorretas[2],   'usuario': sessaonomecompleto})


def obter_rsp_corretas(rspusuariolist):
    rsp = AltQuestion.objects.select_related('qid').annotate(qtextq=F('qid__qtext'), rspcorreta=F('qid__rspcorretaid'), justresposta=F('qid__justresposta')).filter(pk__in=rspusuariolist).values()
    rsplist = (list(rsp))
    for r in rsp:
        g = AltQuestion.objects.get(pk=r['rspcorreta'])
        r['textomeu'] = g.alttexto
    rspcorretas = [rspt['id'] == rspt['rspcorreta'] for rspt in rsplist].count(True)
    textcorr = opcaotexto(rspcorretas, len(rsplist))
    return rspcorretas, rsp, textcorr
