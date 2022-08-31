codigos = {
    "a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".",
    "f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---",
    "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.", "o" : "---",
    "p" : ".--.", "q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-",
    "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--",
    "z" : "--..", "1" : ".----", "2" : "..---", "3" : "...--", 
    "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--....", 
    "8" : "---...", "9" : "----.", "0" : "-----", " " : " "
}

invertido = {value: key for key, value in codigos.items()}

def morse(frase: str) -> str:
    morse = ""
    for i, letra in enumerate(frase):
        morse += codigos.get(letra, f"({letra})")
        if (i+1) < len(frase):
            morse += " "
    return morse

def normal(morse: str) -> str:
    frase = ""
    palavras = morse.split("   ")
    for j, palavra in enumerate(palavras):
        letras = palavra.split(" ")
        for letra in letras:
            frase += invertido.get(letra, f"({letra})")
        if (j+1) < len(palavras):
            frase += " "

    return frase

if __name__ == "__main__":
    # --- ..   - ..- -.. ---   -... . --
    # oi tudo bem /\ /\ /\

    texto = input("Digite um texto a ser convertido a codigo morse:\n")
    codigo_morse = morse(texto)
    print(codigo_morse)

    codigo_morse = input("Digite um codigo morse a ser convertido a texto:\n")
    texto = normal(codigo_morse)
    
    print(texto)





