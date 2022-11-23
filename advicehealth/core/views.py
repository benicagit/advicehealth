from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Proprietario, Veiculo
from .forms import ProprietarioModelForm, VeiculoModelForm


class IndexView(ListView):
    models = Veiculo
    template_name = 'index.html'
    queryset = Veiculo.objects.all()
    context_object_name = 'veiculos'


class CadastroView(TemplateView):
    template_name = 'cadastro.html'


class CadastroVeiculoView(CreateView):
    models = Veiculo
    template_name = 'veiculo_form.html'
    form_class = VeiculoModelForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valido, campo, msg = regras_negocio().qtd_veiculo_proprietario(form)
        if not valido:
            form.add_error(campo, msg)
            return self.form_invalid(form)
        return super(CadastroVeiculoView, self).form_valid(form)


class EditarVeiculoView(UpdateView):
    models = Veiculo
    template_name = 'veiculo_form.html'
    form_class = VeiculoModelForm
    queryset = Veiculo.objects.all()
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        context = super(EditarVeiculoView, self).get_context_data()
        valido, campo, msg = regras_negocio().qtd_veiculo_proprietario(form)
        if not valido:
            form.add_error(campo, msg)
            return self.form_invalid(form)
        
        regras_negocio().oprtunidade_de_venda(form, context)
        return super(EditarVeiculoView, self).form_valid(form)


class ExcluirVeiculoView(DeleteView):
    models = Veiculo
    template_name = 'excluir_veiculo.html'
    queryset = Veiculo.objects.all()
    success_url = reverse_lazy('index')


class ListProprietarioView(ListView):
    models = Proprietario
    template_name = 'lista_proprietario.html'
    queryset = Proprietario.objects.all()
    context_object_name = 'proprietarios'


class CadastroProprietarioView(CreateView):
    models = Proprietario
    template_name = 'proprietario_form.html'
    form_class = ProprietarioModelForm
    success_url = reverse_lazy('lista-proprietario')

    def form_valid(self, form):
        valido, campo, msg = regras_negocio().valida_proprietario(form)
        if not valido:
            form.add_error(campo, msg)
            return self.form_invalid(form)
        return super(CadastroProprietarioView, self).form_valid(form)


class EditarProprietarioView(UpdateView):
    models = Proprietario
    template_name = 'proprietario_form.html'
    form_class = ProprietarioModelForm
    queryset = Proprietario.objects.all()
    success_url = reverse_lazy('lista-proprietario')


class ExcluirProprietarioView(DeleteView):
    models = Proprietario
    template_name = 'excluir_proprietario.html'
    queryset = Proprietario.objects.all()
    success_url = reverse_lazy('lista-proprietario')


class regras_negocio():

    def qtd_veiculo_proprietario(self, form):
        proprietario = form.cleaned_data['proprietario']
        qtd_veiculo_proprietario = Veiculo.objects.filter(proprietario=proprietario).count()

        if qtd_veiculo_proprietario >= 3:
            return False, 'proprietario', 'Esse proprietário já possui 3 veiculos em seu nome'

        if qtd_veiculo_proprietario == 0:
            Proprietario.objects.filter(nome=proprietario).update(oportunidade_de_venda=False)

        return True, '', ''

    def oprtunidade_de_venda(self, form, context):

        id_veiculo = context['veiculo'].id
        proprietario = form.cleaned_data['proprietario']
        obj_veiculo = Veiculo.objects.get(id=id_veiculo)

        if proprietario != obj_veiculo.proprietario:
            qtd_veiculo_proprietario_novo = Veiculo.objects.filter(proprietario=proprietario).count()
            qtd_veiculo_proprietario_atual = Veiculo.objects.filter(proprietario=obj_veiculo.proprietario).count()

            if qtd_veiculo_proprietario_novo == 0:
                Proprietario.objects.filter(nome=proprietario).update(oportunidade_de_venda=False)

            if qtd_veiculo_proprietario_atual == 1:
                Proprietario.objects.filter(nome=obj_veiculo.proprietario).update(oportunidade_de_venda=True)


    def valida_proprietario(self, form):

        cpf = form.cleaned_data['cpf']
        if Proprietario.objects.filter(cpf=cpf).exists():
            return False, 'cpf', 'CPF já cadastrado no sistema. Favor conferir se o proprietário está cadastrado no sistema.'

        return True, '', ''

    def valida_excluir_veiculo(self, context):

        nome_proprietario = context['veiculo'].proprietario

        if Veiculo.objects.filter(proprietario=nome_proprietario).count() == 1:
            Proprietario.objects.filter(id=context['veiculo'].proprietario).update(oportunidade_de_venda=True)
