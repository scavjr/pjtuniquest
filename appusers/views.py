
from django.shortcuts import redirect, render
from appusers.forms import CadUsuarioForm


def cad_usuario(request):
    if request.method == 'POST':
        form = CadUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CadUsuarioForm()
    context = {
            'form': form
         }
    return render(request, 'appusers/appuser_cadusuario.html', context)
