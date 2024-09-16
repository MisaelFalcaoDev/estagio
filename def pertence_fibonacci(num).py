def pertence_fibonacci(num):
    # Primeiros dois termos da sequência
    a, b = 0, 1
    
    # Se o número for 0 ou 1, ele pertence à sequência
    if num == 0 or num == 1:
        return f"O número {num} pertence à sequência de Fibonacci."
    
    # Gera a sequência até ultrapassar ou encontrar o número
    while b <= num:
        if b == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    
    return f"O número {num} NÃO pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero)
print(resultado)
