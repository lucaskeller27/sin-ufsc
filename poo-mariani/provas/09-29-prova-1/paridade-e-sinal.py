# Ler a quantidade N de valores a serem lidos
n = int(input())

# Ler os números
for i in range (n):
    num = int(input())
    
    # Conferir a paridade
    if (num % 2 == 0):
        paridade = 'EVEN'
    else:
        paridade = 'ODD'
    
    # Conferir o sinal
    if (num > 0):
        sinal = 'POSITIVE'
    elif (num < 0):
        sinal = 'NEGATIVE'
    else:
        sinal = 'NULL'