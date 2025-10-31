# Leitura do salário
salario = float(input())

# Cálculo do reajuste salarial
if (salario <= 400.00):
    percentual = 15
elif (salario <= 800.00):
    percentual = 12
elif (salario <= 1200.00):
    percentual = 10
elif (salario <= 2000.00):
    percentual = 7
elif (salario >= 2000.00):
    percentual = 4

# Cálculo do valor de reajuste ganho
reajuste = salario * percentual / 100
salario_novo = salario + reajuste

# Entrega do resultado
print(f"Novo salario: {salario_novo:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %")