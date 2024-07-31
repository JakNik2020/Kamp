n = int(input())
najmanje_a = 0
najmanje_b = 0
najvece_a = 0
najvece_b = 0
for i in range(1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    najmanje_a = x
    najmanje_b = y
    najvece_a = x
    najvece_b = y
for i in range(n - 1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x <= najmanje_a and y <= najmanje_b:
        najmanje_a = x
        najmanje_b = y
    if x >= najvece_a and y >= najvece_b:
        najvece_a = x
        najvece_b = y
nesto_A = najvece_a - najmanje_a
nesto_B = najvece_b - najmanje_b
print(nesto_A * nesto_B)
