#34

# Leitura da matriz D 5x5
D = [list(map(int, input(f"Digite os 5 elementos da linha {i+1} da matriz D: ").split())) for i in range(5)]

# Leitura do valor X
valor_x = int(input("Digite o valor X que deseja procurar na matriz: "))

# Verificando se o valor X existe na matriz
existe = any(valor_x in linha for linha in D)

# Exibindo o resultado
if existe:
    print(f"O valor {valor_x} existe na matriz.")
else:
    print(f"O valor {valor_x} NÃO existe na matriz.")