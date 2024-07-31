n = int(input())
broj = 0
lista = []
for i in range(n):
    x = int(input())
    lista.append(x)
    broj = broj + x
lista.sort()
broj = broj * 10
broj = broj // n
broj = broj / 10
print(broj)
lol = n // 2
print(lista[lol])
