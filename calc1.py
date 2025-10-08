import time

print("------- [ Calculadora ] -------")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Infome o segundo número: "))
time.sleep(1)
operacao = input("Selecione a operação (+,-,*,/): ")
print("-------------------------------")
time.sleep(1)

if operacao == '+':
    resultado = n1 + n2
elif operacao == '-':
    resultado = n1 - n2
elif operacao == '*':
    resultado = n1 * n2
elif operacao == '/':
    if (n2 == 0):
        resultado = "Não é possível dividir por 0"
    else:
        resultado = n1 / n2
else:
    print("Essa não é uma operação disponível.")

print(f"- [ {operacao} ] - O resultado é {resultado}.")

time.sleep(1)
print("-------------------------------")
