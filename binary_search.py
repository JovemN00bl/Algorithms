class Algoritmos:

    def pesquisa_binaria(lista, item):
        low =0
        high = len(lista)

        while low <= high:
            mid = (low + high) // 2
            kick = lista[mid]
            if kick == item:
                return mid
            if kick > item:
                high = mid - 1
            else:
                low = mid + 1
        return None