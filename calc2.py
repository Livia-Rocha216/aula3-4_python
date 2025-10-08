import time

def soma(n1,n2):
    return n1 + n2

def subtracao(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1 * n2

def divisao(n1,n2):
    if (n2 == 0):
        resultado = "Não é possível dividir por 0"
    else:
        return n1 / n2

print("------- [ Calculadora ] -------")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Infome o segundo número: "))
time.sleep(1)
operacao = input("Selecione a operação (+,-,*,/): ")
print("-------------------------------")
time.sleep(1)

if operacao == '+':
    resultado = soma(n1,n2)
elif operacao == '-':
    resultado = subtracao(n1,n2)
elif operacao == '*':
    resultado = multiplicacao(n1,n2)
elif operacao == '/':
    resultado = divisao(n1,n2)
elif operacao != '+' or '-' or '*' or '/':
    print(f"- [ x ] - Essa não é uma operação disponível.")
else:
    print(f"- [ {operacao} ] - O resultado é {resultado}.")


time.sleep(1)
print("-------------------------------")
