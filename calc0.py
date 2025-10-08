import time

print("------- [ Calculadora ] -------")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Infome o segundo número: "))
print("-------------------------------")

time.sleep(1)
resultado = n1 + n2
print(f"- [ Soma ] - O resultado é {resultado}.")

time.sleep(1)
resultado = n1 - n2
print(f"- [ Subtração ] - O resultado é {resultado}.")

time.sleep(1)
resultado = n1 * n2
print(f"- [ Multiplicação ] - O resultado é {resultado}.")

time.sleep(1)
if (n2 == 0):
    print("- [ Divisão ] - Não é possível dividir por 0.")
else:
    resultado = n1 / n2
    print(f"- [ Divisão ] - O resultado é {resultado}.")

time.sleep(1)
print("-------------------------------")