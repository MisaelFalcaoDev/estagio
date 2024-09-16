def verifica_letra_a(string):
    string_minuscula = string.lower()
    contagem = string_minuscula.count('a')
    
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto = input("Informe uma string: ")
verifica_letra_a(texto)
