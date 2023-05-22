lista = []
ile_liczb = int(input("Ile liczb: "))
for i in range(1, ile_liczb+1):
    print(f'Podaj {i} liczbe: ')
    liczba = int(input())
    lista.append(liczba)
print(lista)
n= len(lista)
for i in range(1, n):
    pom = lista[i]
    j=i-1
    while j>=0 and lista[j] > pom:
        lista[j+1] = lista[j]
        j=j-1
    lista[j+1] = pom
print(lista)