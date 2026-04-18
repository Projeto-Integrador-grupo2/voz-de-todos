from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True, db_index=True)
    ativa = models.BooleanField(default=True)

    professor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='salas'
    )

    def __str__(self):
        return f"{self.nome} ({self.codigo})"


class Questao(models.Model):
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name='questoes'
    )

    texto = models.TextField()

    opcao1 = models.CharField(max_length=100)
    opcao2 = models.CharField(max_length=100)
    opcao3 = models.CharField(max_length=100)
    opcao4 = models.CharField(max_length=100)

    correta = models.IntegerField()

    class Meta:
        ordering = ['id']

    def clean(self):
        if self.correta not in [1, 2, 3, 4]:
            raise ValidationError("Resposta correta deve ser entre 1 e 4")

    def __str__(self):
        return self.texto


class Resposta(models.Model):
    aluno_nome = models.CharField(max_length=100, db_index=True)

    questao = models.ForeignKey(
        Questao,
        on_delete=models.CASCADE,
        related_name='respostas'
    )

    resposta = models.IntegerField()
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['aluno_nome', 'questao'],
                name='unique_resposta_aluno'
            )
        ]