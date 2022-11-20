from django.db import models


class Proprietario(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)
    cpf = models.CharField('CPF', max_length=11, blank=False, null=False)
    oportunidade_de_venda = models.BooleanField('Oportunida de Venda', default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Proprietário'
        verbose_name_plural = "Proprietários"


class Veiculo(models.Model):
    COR_CHOICES = (
        ('amarela', 'Amarela'),
        ('azul', 'Azul'),
        ('cinza', 'Cinza')
    )

    TIPO_CHOICES = (
        ('hatch', 'Hatch'),
        ('sedan', 'Sedan'),
        ('conversivel', 'Conversível')
    )

    modelo = models.CharField('Modelo', max_length= 50, blank=False, null=False)
    cor = models.CharField('Cor', max_length=7, choices=COR_CHOICES)
    tipo = models.CharField('Tipo', max_length=11, choices=TIPO_CHOICES)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
