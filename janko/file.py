def prosek(ocene):
    return sum(ocene) / len(ocene)


def prosek_ucenika(ucenici):
    for key in ucenici.keys():
        ucenici[key] = prosek(ucenici[key])


def najveci_prosek(ucenici):
    max_prosek = 0
    max_ucenik = " "
    for key in ucenici.keys():
        if ucenici[key] > max_prosek:
            max_prosek = ucenici[key]
            max_ucenik = key


ucenici = {"stefan": [5, 5, 2], "marko": [3, 4, 5], "jovana": [2, 3, 4]}

print(prosek("stefan"))
proseci = prosek_ucenika(ucenici.copy())
print(proseci)
