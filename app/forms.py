from django import forms
from .models import Sala, Questao

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'codigo', 'ativa']


class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        exclude = ['sala']

    def clean(self):
        cleaned = super().clean()
        correta = cleaned.get("correta")

        if correta not in [1, 2, 3, 4]:
            raise forms.ValidationError("Resposta correta inválida")

        return cleaned