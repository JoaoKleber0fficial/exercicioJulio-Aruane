# Leitura da matriz G 5x5
G = [list(map(int, input(f"Digite os 5 elementos da linha {i+1} da matriz G: ").split())) for i in range(5)]

# Vetores de soma das linhas (SL) e soma das colunas (SC)
SL = [sum(linha) for linha in G]
SC = [sum(G[i][j] for i in range(5)) for j in range(5)]

# Exibindo os resultados
print("Somas das linhas (SL):", SL)
print("Somas das colunas (SC):", SC)