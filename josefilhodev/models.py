from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name_plural = "1 - Skills"  # Nome de exibição plural personalizado

class Certificado(models.Model):
    certificado_name = models.CharField(max_length=100)
    certificado_link = models.URLField()
    instituicao_img = models.URLField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.certificado_name

    class Meta:
        ordering = ['order']
        verbose_name_plural = "2 - Certificados"  # Nome de exibição plural personalizado

class Educacao(models.Model):
    titulo = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    periodo = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['order']
        verbose_name_plural = "3 - Educação"  # Nome de exibição plural personalizado

class Experiencia(models.Model):
    cargo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    periodo = models.CharField(max_length=100)
    descricao = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.cargo

    class Meta:
        ordering = ['order']
        verbose_name_plural = "4 - Experiências"  # Nome de exibição plural personalizado

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.URLField()  # Link para a imagem do projeto
    link = models.URLField()  # Link para o projeto no GitHub ou página relacionada
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['order']
        verbose_name_plural = "5 - Projetos"  # Nome de exibição plural personalizado
