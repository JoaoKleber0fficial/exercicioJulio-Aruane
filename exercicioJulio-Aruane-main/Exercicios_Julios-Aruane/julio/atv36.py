#36

# Leitura da matriz A 12x13
A = [list(map(int, input(f"Digite os 13 elementos da linha {i+1} da matriz A: ").split())) for i in range(12)]

# Modificando a matriz A
for i in range(12):
    maior = max(A[i])
    A[i] = [x / maior for x in A[i]]

# Exibindo a matriz A modificada
for linha in A:
    print(linha)