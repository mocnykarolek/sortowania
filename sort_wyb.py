lista = []
ile_liczb = int(input("Ile liczb: "))
for i in range(1, ile_liczb+1):
    print(f'Podaj {i} liczbe: ')
    liczba = int(input())
    lista.append(liczba)
print(lista)


n= len(lista)

for i in range(n-1):
    m=i
    for j in range(i+1, n):
        if lista[j] < lista[m]:
            m=j
    lista[i], lista[m] = lista[m], lista[i]

print(lista)