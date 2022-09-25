from os import system

def converter(mensagem: str):
    # return mensagem.encode("utf-8").decode("utf-8")
    return mensagem.encode("raw_unicode_escape").decode("unicode_escape")

def criar_fluxo(chave):
    chave = [ord(c) for c in chave]
    fluxo = [n for n in range(256)]

    j = 0
    for i in range(256):
        j = (j + fluxo[i] + chave[i % len(chave)]) % 256
        fluxo[i], fluxo[j] = fluxo[j], fluxo[i]

    return fluxo

def cifra(chave, msg):
    fluxo = criar_fluxo(chave)
    cifrada = []

    j = k = 0
    
    for i in range(len(msg)):
        j = (j + 1) % 256
        k = (k + fluxo[j]) % 256
        fluxo[j], fluxo[k] = (fluxo[k], fluxo[j])
        cifrada.append(fluxo[(fluxo[j] + fluxo[k]) % 256] ^ msg[i]) 
    
    return cifrada

def criptografia(chave, mensagem):
    msg = [ord(c) for c in mensagem]
    print(msg)
    cifrado = cifra(chave, msg)
    
    cifrado = "".join(map(chr, cifrado))
    return cifrado

def descriptografia(chave, mensagem):
    mensagem = converter(mensagem)
    msg = [ord(c) for c in mensagem]
    cifrado = cifra(chave, msg)
    
    cifrado = "".join(map(chr, cifrado))
    return cifrado

def validar_input(msg):
    entrada = input(msg)
    while not entrada:
        print("Entrada invalida")
        entrada = input(msg)
    
    return entrada

def formatar_saida(saida):
    return repr(saida)

system('cls')
CRIPTOGRAFIA = 1
DESCRIPTOGRAFIA = 2
while True:
    print("Menu principal")
    print("[1] Criptografar")
    print("[2] Descriptografar")
    print("[3] Sair")
    opcao = int(input("? "))
    if opcao in (1,2,3):
        if opcao == CRIPTOGRAFIA:
            chave = validar_input("Digite a chave:")
            mensagem = validar_input("Digite a mensagem:")
            criptografada = criptografia(chave, mensagem)
            print(formatar_saida(criptografada))
            
        elif opcao == DESCRIPTOGRAFIA:
            chave = validar_input("Digite a chave:")
            mensagem = validar_input("Digite a mensagem:")
            descriptografada = descriptografia(chave, mensagem)
            print(formatar_saida(descriptografada))
        else:
            break
    else:
        print("Entrada inválida")
        continue