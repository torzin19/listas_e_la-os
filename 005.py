# Listas iniciais fornecidas no desafio
itens = ["pizza", "suco", "bolo", "refrigerante"]
precos = [10, 5, 7, 8]
total_compra = 0

print("--- Cardápio da Cantina ---")

# 1. Mostrar os itens do cardápio e os seus preços
for i in range(len(itens)):
    print(f"{i} - {itens[i]}: R$ {precos[i]:.2f}")

print("\nDigite -1 para encerrar o pedido.")

# 2. Permitir, com while, que os usuários escolham os itens pelo número
while True:
    escolha = int(input("\nEscolha o número do item: "))
    
    # 4. Encerrar a escolha ao digitar -1
    if escolha == -1:
        break
        
    # Verifica se o número digitado corresponde a um item válido da lista
    if 0 <= escolha < len(itens):
        # 3. Somar o valor de cada item escolhido
        total_compra += precos[escolha]
        print(f"Adicionado: {itens[escolha]} (R$ {precos[escolha]:.2f})")
    else:
        print("Opção inválida! Digite um número correspondente ao cardápio.")

# 5. Mostrar o valor total da compra
print("\n--- Resumo do Pedido ---")
print(f"Valor total da compra: R$ {total_compra:.2f}")