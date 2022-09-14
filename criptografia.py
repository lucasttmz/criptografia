def menu_principal() -> int:
    print("Menu Principal")
    print("- 1: Criptografar")
    print("- 2: Decriptografar")
    print("- 3: Sair")

    entrada = input("? ")
    while entrada not in ("1", "2", "3"):
        print("Entrada inválida")
        entrada = input("? ")
    
    return int(entrada)

def validar_input(msg: str) -> str:
    entrada = input(msg)
    while not entrada:
        print("Entrada vazia\n")
        entrada = input(msg)

    return entrada

def criptografar(chave: str, msg: str) -> str:
    return f"{msg} so que criptografada"

def decriptografar(chave: str, msg: str) -> str:
    return f"{msg} so que decriptografada"



if __name__ == "__main__":
    CRIPTOGRAFAR = 1
    DECRIPTOGRAFAR = 2
    SAIR = 3

    while True:
        opcao = menu_principal()
        if opcao != SAIR:
            chave = validar_input("Digite a chave:\n")
            msg = validar_input("Digite a mensagem:\n")
            if opcao == CRIPTOGRAFAR:
                saida = criptografar(chave, msg)
                print(f"Mensagem criptografada:\n{saida}\n")
            elif opcao == DECRIPTOGRAFAR:
                saida = decriptografar(chave, msg)
                print(f"Mensagem decriptografada:\n{saida}\n")
        else:
            break