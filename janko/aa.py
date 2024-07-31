a = int(input())
broj = a
nesto = 0
for i in range(a - 2):
    broj = broj - 1
    if a / broj == a // broj:
        nesto = broj
if nesto == 0:
    print("jeste")
else:
    print(nesto)
