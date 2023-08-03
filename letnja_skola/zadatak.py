studenti = {
    "RA 112/2021":{"ime":"Marko" , "prezime":"Petrović","godina studija":4,"ocene":[5,4,2,4,5,3,5,3,5,4],"prosek":3.9},
    "IN 142/2023":{"ime":"Luka" , "prezime":"Liković","godina studija":2,"ocene":[2,4,3,1,2,2,3,4,1,1],"prosek":2.3},
    "CA 092/2020":{"ime":"Lena" , "prezime":"Okolović","godina studija":3,"ocene":[1,3,2,1,1,1,2,2,1,3],"prosek":1.7},
    "LF 001/2021":{"ime":"Ana" , "prezime":"Štreberović","godina studija":1,"ocene":[5,5,4,5,5,5,4,4,5,5],"prosek":4.8}
    }
ocene = []
broj = int(input())
for i in range(broj):
    šifra = input("ubacite šifru vašeg studenta ")
    ime = input("ubacite ime ")
    prezime = input("ubacite prezime ")
    godina_studija = int(input("ubacite godinu studija "))
    br_ocena = int(input("ubacite koliko on ima ocena "))
    for i in range(br_ocena):
        x = int(input())
        ocene.append(x)
        broj = broj + x
    prosek = broj / len(ocene) - 0.1
    studenti[f"šifra"] = {"ime" : ime , "prezime":prezime , "godina_studija":godina_studija , "ocene":ocene , "prosek":prosek}
print(studenti)