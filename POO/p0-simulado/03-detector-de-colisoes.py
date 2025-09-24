# Leitura dos valores dos dois retângulos
x1a, y1a, x2a, y2a = [int(w) for w in input().split()] # A
x1b, y1b, x2b, y2b = [int(w) for w in input().split()] # B

# Colocar os valores em ordem crescente
ax1, ax2 = min(x1a, x2a), max(x1a, x2a) # X do A
ay1, ay2 = min(y1a, y2a), max(y1a, y2a) # Y do A
bx1, bx2 = min(x1b, x2b), max(x1b, x2b) # X do B
by1, by2 = min(y1b, y2b), max(y1b, y2b) # Y do B

# Verificar se NÃO HÁ interseção
if (ax2 < bx1) or (bx2 < ax1) or (ay2 < by1) or (by2 < ay1):
    print(0)
else:
    print(1)