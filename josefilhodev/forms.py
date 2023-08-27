from django import forms
from .models import Certificado, Educacao, Experiencia, Projeto


class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = ['certificado_name', 'certificado_link', 'instituicao_img']


class EducacaoForm(forms.ModelForm):
    class Meta:
        model = Educacao
        fields = '__all__'

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = '__all__'

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'