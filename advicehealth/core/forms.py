from django.forms import ModelForm
from .models import Proprietario, Veiculo

class ProprietarioModelForm(ModelForm):
    class Meta:
        model = Proprietario
        fields = ['nome', 'cpf', 'oportunidade_de_venda']


class VeiculoModelForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'cor', 'tipo', 'proprietario']
