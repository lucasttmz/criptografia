def cifra(msg: str, r_cifra: int, r_embaralhar: int) -> str:
    alfabeto = [chr(97+n) for n in range(26)]
    saida = ""

    for letra in msg:
        if letra not in alfabeto:
            saida += letra
        else:
            saida += alfabeto[(alfabeto.index(letra) + r_cifra) % 26]
    
    print(f"Antes do embaralhamento: {saida}")

    return embaralhar(saida, r_embaralhar)

def embaralhar(msg: str, x: int) -> str:
    saida = ""
    palavras = msg.split(" ")

    for palavra in palavras:
        for i in range(len(palavra)):
            saida += palavra[(i+x) % len(palavra)]
        saida += " "
    
    saida = saida.rstrip()
    print(f"Depois do embaralhamento: {saida}")

    return saida

if __name__ == "__main__":
    entrada = "tudo bem com vc"
    print(f"Msg: {entrada}")

    cifra_ = cifra(entrada, 1, 2)