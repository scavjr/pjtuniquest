from django.shortcuts import redirect, render
from apphome.forms import login_form
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from apphome.models import ListQuestAtual
from appquest.models import Assunto, Curso, Questions


def home(request):
    assuntos = ['']  # obter_assunto(request)
    cursos = obter_cursos(request)
    lista_atual = obter_list_atual()
    qtd_q= qtd_questoes()
    if request.method == 'GET':
        #request.session["logado"] = True
        nomecompleto = request.session.get('sessaonomecompleto')

        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            return render(request, 'apphome/apphome_dashboard.html', {"username": request.user.username, 'usuario': nomecompleto,'qtd_q': qtd_q, 'cursos': cursos, 'assuntos': assuntos, 'lista_atual': lista_atual})
        else:
            form = login_form(request)
            return render(request, 'apphome/apphome_login.html', {"form": form})
    else:
        if 'logar' in request.POST:
            user = login_usuario(request)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    nomecompleto = user.get_full_name()
                    request.session["sessaonomecompleto"] = nomecompleto
                    return render(request, 'apphome/apphome_dashboard.html', {"username": request.user.username, 'usuario': nomecompleto, 'cursos': cursos, 'user': user,
                                                                              'assuntos': assuntos, 'lista_atual': lista_atual, 'qtd_q': qtd_q})
            else:
                msgerro = "Credenciais não autorizadas!"
                form = login_form(request)
                return render(request, 'apphome/apphome_login.html', {"form": form, 'msgerro': msgerro})
        elif 'registrar' in request.POST:
            return redirect('users/cadastro_users')
        elif 'Register' in request.POST:
            return render(request, 'apphome/apphome_login.html', {})


def login_usuario(request):
    usuario = list(request.POST.values())[1]
    password = list(request.POST.values())[2]
    user = authenticate(username=usuario, password=password)
    return user


def logout_view(request):
    logout(request)
    return redirect('home')


def obter_assunto(request):
    assunto_list = Assunto.objects.all()
    return assunto_list


def obter_list_atual():
    list_atual = ListQuestAtual.objects.all()
    return list_atual


def obter_cursos(request):
    cursos_list = Curso.objects.all().values_list()
    return cursos_list

def qtd_questoes():
    questoes_count = Questions.objects.all().count()
    print(questoes_count)
    return questoes_count