def sortowanie_bombelkowe(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = []
ile_liczb = int(input("Ile liczb: "))
for i in range(1, ile_liczb+1):
    print(f'Podaj {i} liczbe: ')
    liczba = int(input())
    lista.append(liczba)
print(lista)
posortowane = sortowanie_bombelkowe(lista)
print(posortowane)








