from os import system

def gerar_fluxo(chave: str) -> list[int]:
    chave = [ord(char) for char in chave]
    fluxo = [n for n in range(256)]
    j = 0

    for i in range(256):
        j = (j + fluxo[i] + chave[i % len(chave)]) % 256
        fluxo[i], fluxo[j] = (fluxo[j], fluxo[i])

    return fluxo

def cifra(fluxo: list[int], mensagem: list[int]) -> list[int]:
    msg_cifrada = []
    j = k = 0
    
    for i in range(len(mensagem)):
        j = (j + 1) % 256
        k = (k + fluxo[j]) % 256
        fluxo[j], fluxo[k] = (fluxo[k], fluxo[j])
        c = (fluxo[(fluxo[j] + fluxo[k]) % 256] ^ mensagem[i])
        msg_cifrada.append(c) 
    
    return msg_cifrada

def criptografar(chave: str, mensagem: str) -> str:
    mensagem = [ord(char) for char in mensagem]
    fluxo = gerar_fluxo(chave)
    cifrado = cifra(fluxo, mensagem)
    criptografado = "".join(map(chr, cifrado))

    return criptografado

def descriptografar(chave: str, mensagem: str) -> str:
    mensagem = formatar_entrada(mensagem)
    descriptografado = criptografar(chave, mensagem)

    return descriptografado

def menu_principal() -> int:
    print("Menu Principal")
    print("[1] Criptografar")
    print("[2] Descriptografar")
    print("[3] Sair")

    entrada = input(">>> ")
    while entrada not in ("1", "2", "3"):
        print("Entrada inválida")
        entrada = input(">>> ")
    
    return int(entrada)

def validar_input(mensagem: str) -> str:
    entrada = input(mensagem)
    while not entrada:
        print("Entrada inválida")
        entrada = input(mensagem)
    
    return entrada

def formatar_entrada(entrada: str) -> str:
    return entrada.encode("raw_unicode_escape").decode("unicode_escape")

def formatar_saida(saida: str) -> str:
    return repr(saida)[1:-1]


if __name__ == "__main__":
    CRIPTOGRAFAR = 1
    DESCRIPTOGRAFAR = 2
    SAIR = 3

    system('cls')
    opcao = menu_principal()
    while opcao != SAIR:
        system('cls')
        print(("Criptografia", "Descriptografia")[opcao-1])
        chave = validar_input("Digite a chave:\n")
        mensagem = validar_input("Digite a mensagem:\n")
        if opcao == CRIPTOGRAFAR:
            saida = criptografar(chave, mensagem)
            print("Mensagem criptografada:")
        elif opcao == DESCRIPTOGRAFAR:
            saida = descriptografar(chave, mensagem)
            print("Mensagem descriptografada:")

        print(formatar_saida(saida))
        input()
        system('cls')
        opcao = menu_principal()

    # system('cls')
    # opcao = menu_principal()
    # while opcao != SAIR:
    #     system('cls')
    #     if opcao == CRIPTOGRAFAR:
    #         print("Criptografar")
    #         chave = validar_input("Digite a chave:\n")
    #         mensagem = validar_input("Digite a mensagem:\n")
    #         saida = criptografar(chave, mensagem)
    #         print("Mensagem criptografada:")
    #     elif opcao == DESCRIPTOGRAFAR:
    #         print("Descriptografar")
    #         chave = validar_input("Digite a chave:\n")
    #         mensagem = validar_input("Digite a mensagem:\n")
    #         saida = descriptografar(chave, mensagem)
    #         print("Mensagem descriptografada:")

    #     print(formatar_saida(saida))
    #     input()
    #     system('cls')
    #     opcao = menu_principal()

    
    

