grafo = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2

grafo['a'] = {}
grafo['a']['fim'] = 1

grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5

grafo['fim'] = {}

infinito = float("inf")
custos = {}
custos['a'] = 6
custos['b'] = 2
custos['fim'] = infinito

pais = {}
pais['a'] = "inicio"
pais['b'] = "inicio"
pais["fim"] = None

processados = []


def ache_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for node in custos:
        custo = custos[node]
        if custo < custo_mais_baixo and node not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = node
    return nodo_custo_mais_baixo

node = ache_custo_mais_baixo(custos)
while node is not None:
    custo = custos[node]
    vizinhos = grafo[node]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = node
    processados.append(node)
    node = ache_custo_mais_baixo(custos)


print(custos)



