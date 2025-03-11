# 32

# Leitura da matriz A 4x6
A = []
for i in range(4):
    while True:
        try:
            # Garantir que o usuário digite exatamente 6 números
            linha = list(map(int, input(f"Digite os 6 elementos da linha {i+1} da matriz A (separe por espaço): ").split()))
            if len(linha) == 6:  # Verifique se a linha tem exatamente 6 elementos
                A.append(linha)
                break
            else:
                print("Por favor, digite exatamente 6 números.")
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar números inteiros.")

# Leitura da matriz B 4x6
B = []
for i in range(4):
    while True:
        try:
            linha = list(map(int, input(f"Digite os 6 elementos da linha {i+1} da matriz B: ").split()))
            if len(linha) == 6:
                B.append(linha)
                break
            else:
                print("Por favor, digite exatamente 6 números.")
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar números inteiros.")

# a) Matriz S (soma de A e B)
S = [[A[i][j] + B[i][j] for j in range(6)] for i in range(4)]

# b) Matriz D (diferença de A e B)
D = [[A[i][j] - B[i][j] for j in range(6)] for i in range(4)]

# Exibindo as matrizes S e D
print("\nMatriz S (Soma de A e B):")
for linha in S:
    print(linha)

print("\nMatriz D (Diferença de A e B):")
for linha in D:
    print(linha)