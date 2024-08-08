# Receber o primeiro número inteiro do usuário
numero1 = int(input("Digite o primeiro número inteiro: "))

# Receber o segundo número inteiro do usuário
numero2 = int(input("Digite o segundo número inteiro: "))

# Realizar as operações matemáticas
soma = numero1 + numero2
subtracao = abs(numero1 - numero2)  # Garantir valor absoluto
multiplicacao = numero1 * numero2

# Verificar se o segundo número é diferente de zero para evitar divisão por zero
if numero2 != 0:
    divisao = numero1 // numero2  # Divisão inteira
else:
    divisao = "Indefinida (divisão por zero não permitida)"

# Exibir os resultados
print("Resultados das operações entre os dois números:")
print(f"Soma: {numero1} + {numero2} = {soma}")
print(f"Subtração (valor absoluto): |{numero1} - {numero2}| = {subtracao}")
print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")
print(f"Divisão inteira: {numero1} // {numero2} = {divisao}")
