def todos_pares_somam(vetor, alvo):
    vetor.sort()
    left, right = 0, len(vetor) - 1
    pares = []
    while left < right:
        soma = vetor[left] + vetor[right]
        if soma == alvo:
            pares.append((vetor[left], vetor[right]))
            left, right = left + 1, right - 1
        elif soma < alvo:
            left += 1
        else:
            right -= 1
    if not pares:
        return "Nenhum par encontrado"
    return pares

vetor = [1, 3, 6, 7, 8, 9, 10, 11, 12, 18]
alvo = 15

resultado = todos_pares_somam(vetor, alvo)
print(resultado)