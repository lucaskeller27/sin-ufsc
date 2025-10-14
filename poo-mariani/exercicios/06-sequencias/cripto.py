# Componentes
# 1. Alfabeto normal
# 2. Alfabeto para cifragem
# 3. Mensagem cifrada

# Implementar um programa que dados estes 3 componentes retorne a mensagem original. Cada um destes componentes está numa linha distinta.

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
mapeamento = dict(zip(alfabeto, cifra))

# Leitura do texto criptografado
texto_cripto = input()
texto = ''

for car in texto_cripto:
    if car in mapeamento:
        texto += car