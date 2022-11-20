from django.urls import path
from .views import  indexView, cadastroView


urlpatterns = [
    path('', indexView, name='index'),
    path('cadastro/', cadastroView, name='cadastro'),
    # path('cadastro-veiculo/', CadastroVeiculoView.as_view(), name='cadastro-veiculo'),
    # path('cadastro-proprietario/', CadastroProprietarioView.as_view(), name='cadastro-proprietario'),
    # path('lista-proprietario/', ListProprietarioView.as_view(), name='lista-proprietario'),
    # path('editar-proprietario/<int:pk>/', EditarProprietarioView.as_view(), name='editar-proprietario'),
    # path('excluir-proprietario/<int:pk>/', ExcluirProprietarioView.as_view(), name='excluir-proprietario'),
    # path('editar-veiculo/<int:pk>/', EditarVeiculoView.as_view(), name='editar-veiculo'),
    # path('excluir-veiculo/<int:pk>/', ExcluirVeiculoView.as_view(), name='excluir-veiculo'),
]
