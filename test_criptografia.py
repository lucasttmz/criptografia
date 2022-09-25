"""Arquivo para testes de unidade"""

from criptografia import criptografar

def criptografar_teste(chave: str, mensagem: str) -> None:
    """ Realiza o teste para verificar se a mensagem original
    é igual a descriptografada, caso conrtrário, retorna um erro. """
    criptografado = criptografar(chave, mensagem)
    descriptografado = criptografar(chave, criptografado)

    assert mensagem == descriptografado


def testes():
    """
    Chama a função criptografar_teste para testar cada caso.
    Teste para varios casos especificos, todos com sucesso.
    """
    #Normal
    criptografar_teste(chave="Chave inserida aqui para criar o fluxo", 
                       mensagem="Mensagem a ser criptografada")

    #Numeros
    criptografar_teste(chave="123454321013245684844512", 
                       mensagem="543212345432115616558")

    #Char Especial
    criptografar_teste(chave="#+@ $_% ^-&=D ]-[()", 
                       mensagem="@#@!@#$12_= 123*48abc84 @&#@#")

    #Char Escape
    criptografar_teste(chave="\t123\t321\n__\-", 
                       mensagem="\r123\n242GG82\t11")

    #Mensagem Longa
    criptografar_teste(chave="abcdefghijklkmsmhent",
                       mensagem="aaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaaaabcde" +
                       "aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaa aaaaaabcde" +
                       "aaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaabcde" +
                       "aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaa aaaaaabcde" +
                       "aaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaabcde")

    #Chave Longa
    criptografar_teste(chave="aaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaa aaaaaabcde" +
                       "aaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaabcde" +
                       "aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaa aaaaaaabcde" +
                       "aaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaabcde" +
                       "aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaa aaaaaabcde", 
                       mensagem="abcdefghijklmnopqrstuvwyxz123456790")

    #Ambos Longos
    criptografar_teste(chave="@@lskiia__ sajidij lalislooo sjiajisjjssisabcde" +
                       "@@lskiia__ sajidij lallaoiislooo sjiajisjaijssisabcde" +
                       "@@lskiia__ sajidij lallaoiislooo sjiajisjaijssisabcde" +
                       "@@lskiia__ sajidij lallaoiislooo sjiajisjjisjaijssise" +
                       "@@lskiia__ sajidij lallaoiislooo sjiajjaijssisabcde", 
                       mensagem="aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaabcde" +
                       "aaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                       "aaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaabcde" +
                       "aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaabcde" +
                       "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaabcde")
    
    #Chave com apenas um espaço em branco
    criptografar_teste(chave=" ", 
                       mensagem="A chave esta com um espaco em branco")

    #Mensagem com apenas um espaço em branco
    criptografar_teste(chave="A mensagem esta com um espaco em branco",
                       mensagem=" ")

    #Se um dos testes não der True essa mensagem não aparece
    print("Se essa mensagem apareceu, tudo funcionou como deveria")

if __name__ == "__main__":
    testes()