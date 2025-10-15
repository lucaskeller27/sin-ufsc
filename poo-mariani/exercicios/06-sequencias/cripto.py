# - Ver função "zip"

# Exemplo de entrada:

# abcdefghijklmnopqrstuvwxyz
# PORTUGALBCDEFHIJKMNQSVWXYZ
# GSCPF QITIN TUJMUNNP! GIFIN TUNRIOUMQIN!

# Saída:

# fujam todos depressa! fomos descobertos!

# Pegar letra por letra do texto cifrado, e encontrar a posição da letra no alfabeto cifrado
# Pegar a letra equivalente do alfabeto normal para cada letra do texto cifrado

# Leitura e mapeamento dos alfabetos 
alfabeto = input()
cifra = input()
mapeamento = dict(zip(cifra, alfabeto))

# Leitura do texto criptografado
texto_cripto = input()
texto = ''

for car in texto_cripto:
    if car in mapeamento:
        texto += mapeamento[car]
    else:
        texto += car

print(texto)