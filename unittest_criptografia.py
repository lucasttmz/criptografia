"""Arquivo para testes de unidade utilizando a biblioteca unittest"""

from unittest import TestCase, main
from criptografia import criptografar

class TestCriptografia(TestCase):
    @classmethod
    def setUpClass(cls):
        print('Realizando o teste para verificar se a mensagem original é ' +
              'igual a descriptografada:\n')

    def test_string(self):
        chave = "Chave"
        mensagem = "Mensagem"
        criptografado = criptografar(chave, mensagem)
        descriptografado = criptografar(chave, criptografado)

        self.assertEqual(mensagem, descriptografado)

    def test_numeros(self):
        chave = "12345"
        mensagem = "54321"
        criptografado = criptografar(chave, mensagem)
        descriptografado = criptografar(chave, criptografado)

        self.assertEqual(mensagem, descriptografado)
    
    def test_especial(self):
        chave = "#+@ $_% ^-&=D"
        mensagem = "@#@!@#$12_= 1232*488484 @&#@#"
        criptografado = criptografar(chave, mensagem)
        descriptografado = criptografar(chave, criptografado)

        self.assertEqual(mensagem, descriptografado)
    
    def test_escape(self):
        chave = "\t123\t321"
        mensagem = "\r123\n242"
        criptografado = criptografar(chave, mensagem)
        descriptografado = criptografar(chave, criptografado)

        self.assertEqual(mensagem, descriptografado)
    
    def test_chave_longa(self):
        chave = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde")
        mensagem = " "
        criptografado = criptografar(chave, mensagem)
        descriptografado = criptografar(chave, criptografado)

        self.assertEqual(mensagem, descriptografado)

    def test_msg_longa(self):
        chave = " "
        mensagem = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde")
        criptografado = criptografar(chave, mensagem)
        descriptografado = criptografar(chave, criptografado)

        self.assertEqual(mensagem, descriptografado)
    
    def test_ambos_longos(self):
        chave = ("@@lskiia__ sajidij lallaoiislooo sjiajisjjisjaijssisabcde" +
                 "@@lskiia__ sajidij lallaoiislooo sjiajisjjisjaijssisabcde" +
                 "@@lskiia__ sajidij lallaoiislooo sjiajisjjisjaijssisabcde" +
                 "@@lskiia__ sajidij lallaoiislooo sjiajisjjisjaijssisabcde" +
                 "@@lskiia__ sajidij lallaoiislooo sjiajisjjisjaijssisabcde")
        mensagem = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde")
        criptografado = criptografar(chave, mensagem)
        descriptografado = criptografar(chave, criptografado)

        self.assertEqual(mensagem, descriptografado)
    


if __name__ == "__main__":
    main(verbosity=2)
    