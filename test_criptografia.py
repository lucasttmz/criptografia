"""Arquivo para testes de unidade"""

from criptografia import criptografar

def criptografar_teste(chave: str, mensagem: str) -> None:
    """ Realiza o teste para verificar se a mensagem original
    é igual a descriptografada, caso conrtrário, retorna um erro. """
    criptografado = criptografar(chave, mensagem)
    descriptografado = criptografar(chave, criptografado)

    assert mensagem == descriptografado


def testes():
    """ Chama a função criptografar_teste para testar cada caso. """
    criptografar_teste("Chave", "Mensagem")
    criptografar_teste("12345", "54321")
    criptografar_teste("Fluxo de uma chave", "Criptografia RC4")
    criptografar_teste("#######", "aaaaaa")
    criptografar_teste("abcabc", "   ")
    criptografar_teste("#143124$@@342 213@# 2", "%$433453%#$32 $#@$@")
    criptografar_teste("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
                       "sojdoasjodijosjdojsojdojasodjosjaosdjosjodajosjdoajdo")
    criptografar_teste(" ", "\r123\n242")
    criptografar_teste("[]22441]", "99283xXa")

    print("Se essa mensagem apareceu, tudo funcionou como deveria")

if __name__ == "__main__":
    testes()