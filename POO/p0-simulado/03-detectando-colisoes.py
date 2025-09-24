# Leitura dos valores dos dois retângulos
x1, y1, x2, y2 = [int(w) for w in input().split()] # A
x3, y3, x4, y4 = [int(w) for w in input().split()] # B

# Verificar se não há interseção
if (x1 > x3) or (x1 > x4) or (x2 > x3) or (x2 > x4) or (y1 > y3) or (y1 > y4) or (y2 > y3) or (y2 > y4):
    print(0)
else:
    print(1)