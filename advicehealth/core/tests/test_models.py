from django.test import TestCase
from model_mommy import mommy


class ProprietarioTestCase(TestCase):

    def setUp(self):
        self.proprietario = mommy.make('Proprietario')

    def test_str(self):
        self.assertEquals(str(self.proprietario), self.proprietario.nome)


