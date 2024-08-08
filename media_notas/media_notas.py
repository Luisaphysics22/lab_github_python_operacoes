# Receber as três notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média aritmética
media = (nota1 + nota2 + nota3) / 3

# Exibir o resultado com uma casa decimal
print(f"A média aritmética das notas é: {media:.1f}")
