from os import system

def gerar_fluxo(chave: str) -> list[int]:
    """Gera o fluxo da chave"""
    chave = [ord(c) for c in chave]
    fluxo = [n for n in range(256)]
    j = 0

    for i in range(256):
        j = (j + fluxo[i] + chave[i % len(chave)]) % 256
        fluxo[i], fluxo[j] = (fluxo[j], fluxo[i])

    return fluxo

def cifra(chave: str, msg: str) -> list[int]:
    """Aplica a cifra RC4 na mensagem usando o fluxo da chave"""
    fluxo = gerar_fluxo(chave)
    msg_cifrada = []
    j = k = 0
    
    for i in range(len(msg)):
        j = (j + 1) % 256
        k = (k + fluxo[j]) % 256
        fluxo[j], fluxo[k] = (fluxo[k], fluxo[j])
        msg_cifrada.append(fluxo[(fluxo[j] + fluxo[k]) % 256] ^ msg[i]) 
    
    return msg_cifrada

def criptografar(chave: str, mensagem: str) -> str:
    mensagem = [ord(c) for c in mensagem]
    cifrado = cifra(chave, mensagem)
    
    criptografado = "".join(map(chr, cifrado))
    return criptografado

def descriptografar(chave: str, mensagem: str) -> str:
    mensagem = formatar_entrada(mensagem)
    mensagem = [ord(c) for c in mensagem]
    cifrado = cifra(chave, mensagem)
    
    descriptografado = "".join(map(chr, cifrado))
    return descriptografado

def menu_principal() -> int:
    """Exibe as opções válidas e garante que o input seja válido"""
    print("Menu principal")
    print("[1] Criptografar")
    print("[2] Descriptografar")
    print("[3] Sair")

    entrada = input(">>> ")
    while entrada not in ("1", "2", "3"):
        print("Entrada inválida")
        entrada = input(">>> ")
    
    return int(entrada)

def validar_input(mensagem) -> str:
    """Valida o input do usuário"""
    entrada = input(mensagem)
    while not entrada:
        print("Entrada invalida")
        entrada = input(mensagem)
    
    return entrada

def formatar_entrada(entrada: str) -> str:
    """Em caso de a entrada tiver caracteres em sua representação hexadecimal"""
    return entrada.encode("raw_unicode_escape").decode("unicode_escape")

def formatar_saida(saida: str) -> str:
    """Em caso de a saída tiver caracteres não printáveis,
    troca os caracteres não printáveis por sua representação hexadecimal"""
    return repr(saida)[1:-1]

if __name__ == "__main__":
    CRIPTOGRAFAR = 1
    DESCRIPTOGRAFAR = 2
    SAIR = 3

    system('cls')
    
    while True:
        opcao = menu_principal()
        if opcao != SAIR:
            chave = validar_input("Digite a chave:\n")
            mensagem = validar_input("Digite a mensagem:\n")
            if opcao == CRIPTOGRAFAR:
                saida = criptografar(chave, mensagem)
                print("Mensagem criptografada:")
            elif opcao == DESCRIPTOGRAFAR:
                saida = descriptografar(chave, mensagem)
                print("Mensagem descriptografada:")

            print(formatar_saida(saida))
        else:
            break