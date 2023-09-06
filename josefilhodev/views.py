from django.shortcuts import render

from .models import Skill, Certificado, Educacao, Experiencia, Projeto
from .forms import CertificadoForm, ProjetoForm


def index(request):
    skills = Skill.objects.all()
    certificados = Certificado.objects.all()
    educacoes = Educacao.objects.all()
    experiencias = Experiencia.objects.all()
    projetos = Projeto.objects.all()


    certificado_form = CertificadoForm(request.POST or None)
    projeto_form = ProjetoForm(request.POST or None)

    if request.method == 'POST':
        if certificado_form.is_valid():
            certificado_form.save()

        if projeto_form.is_valid():
            projeto_form.save()

    return render(request, 'index.html',
                  {'skills': skills, 'certificados': certificados, 'educacoes': educacoes,
                   'experiencias': experiencias, 'projetos': projetos,
                   'projeto_form': projeto_form})

