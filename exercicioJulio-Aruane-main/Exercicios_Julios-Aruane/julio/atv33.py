# Leitura da matriz A (4x4)
A = [list(map(int, input(f"Digite os 4 elementos da linha {i+1} da matriz A (separe por espaço): ").split())) for i in range(4)]

# Somar os elementos que têm 'X'
soma_x = 0

# De acordo com os índices da matriz, os elementos que correspondem ao padrão 'X' são:
# Linha 1: A[0][0], A[0][1]
# Linha 2: A[1][0], A[1][1]
# Linha 4: A[3][2], A[3][3]

# Elementos que vão ser somados
indices_x = [(0, 0), (0, 1), (1, 0), (1, 1), (3, 2), (3, 3)]

# Calculando a soma
for i, j in indices_x:
    soma_x += A[i][j]

# Exibindo o resultado
print(f"Soma dos elementos marcados com X: {soma_x}")