cotacao = 5.40

print("1 - Real para Dólar")
print("2 - Dólar para Real")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    valor = float(input("Digite o valor em reais: "))
    resultado = valor / cotacao
    print(f"Valor em dólares: US$ {resultado:.2f}")

elif opcao == 2:
    valor = float(input("Digite o valor em dólares: "))
    resultado = valor * cotacao
    print(f"Valor em reais: R$ {resultado:.2f}")

else:
    print("Opção inválida.")