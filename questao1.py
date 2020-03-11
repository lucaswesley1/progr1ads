valor_litro = float(input("informe o valor do litro: "))
valor_real = float(input("quanto quer abastecer?"))
litro = valor_real / valor_litro
print("com R$ %.2f o veiculo vai recebe %.2f litros." % (valor_real,litro))
