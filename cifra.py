def cifra(msg: str, r_cifra: int, r_embaralhar: int) -> str:
    alfabeto = [chr(97+n) for n in range(26)]
    saida = ""

    for letra in msg:
        if letra not in alfabeto:
            saida += letra
        else:
            saida += alfabeto[(alfabeto.index(letra) + r_cifra) % 26]

    return embaralhar(saida, r_embaralhar)

def embaralhar(msg: str, x: int) -> str:
    print(f"Antes do embaralhamento: {msg}")

    saida = ""
    palavras = msg.split(" ")

    for palavra in palavras:
        for i in range(len(palavra)):
            saida += palavra[(i+x) % len(palavra)]
        saida += " "
    
    return saida.rstrip()

if __name__ == "__main__":
    entrada = input("Digite a mensagem a ser criptografada:\n> ")
    cifra_ = cifra(entrada, 1, 2)
    print(f"Criptografada: {cifra_}")
