# Atividade 31

# Criando uma matriz 5x5 e preenchendo com valores
M = []
for i in range(5):
    # Certifique-se de que o usuário digite 5 números por linha
    while True:
        try:
            linha = list(map(int, input(f"Digite os 5 elementos da linha {i+1} da matriz (separados por espaço): ").split()))
            if len(linha) == 5:  # Verifique se a linha tem exatamente 5 elementos
                M.append(linha)
                break
            else:
                print("Por favor, digite exatamente 5 números.")
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar números inteiros.")

# a) Soma da linha 3
soma_linha_3 = sum(M[2])

# b) Soma da coluna 2
soma_coluna_2 = sum(M[i][1] for i in range(5))

# c) Soma da diagonal principal
soma_diagonal_principal = sum(M[i][i] for i in range(5))

# d) Soma da diagonal secundária
soma_diagonal_secundaria = sum(M[i][4-i] for i in range(5))

# e) Soma de todos os elementos da matriz
soma_total = sum(sum(linha) for linha in M)

# Exibindo os resultados
print(f"Soma da linha 3: {soma_linha_3}")
print(f"Soma da coluna 2: {soma_coluna_2}")
print(f"Soma da diagonal principal: {soma_diagonal_principal}")
print(f"Soma da diagonal secundária: {soma_diagonal_secundaria}")
print(f"Soma de todos os elementos da matriz: {soma_total}")