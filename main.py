class Egzemplarz():
    def __init__ (self, tytul, autor, rokWydania, wypozyczony):
        self.tytul = str(tytul)
        self.autor = str(autor)
        self.rokWydania = int(rokWydania)
        self.wypozyczony = wypozyczony

    def dodaj_egzemplarz(self, egzemplarze): 
        egzemplarze.append(Egzemplarz(self.tytul, self.autor, self.rokWydania, self.wypozyczony))
        return True

    def wypozycz_egzemplarz(tytul, egzemplarze):
        egzTF = False
        for i in range(len(egzemplarze)):
            egzemplarz = egzemplarze[i]
            if egzemplarz.tytul == tytul and egzemplarz.wypozyczony == False:
                egzemplarz.wypozyczony = True
                egzTF = True
        return egzTF

    def oddaj_egzemplarz(tytul, egzemplarze):
        egzTF = False
        for i in range(len(egzemplarze)):
            egzemplarz = egzemplarze[i]
            if egzemplarz.tytul == tytul and egzemplarz.wypozyczony == True:
                egzemplarz.wypozyczony = False
                egzTF = True
        return egzTF


class Czytelnik():
    def __init__(self, nazwisko):
        self.nazwisko = nazwisko

    def dodaj_czytelnika(self, czytelnicy):
        czytelnicy.append(Czytelnik(self.nazwisko))

    def sprawdz_czy_czytelnik_jest_na_liscie(czytelnicy, nazwisko):
      for i in range(len(czytelnicy)):
        temp = czytelnicy[i]
        if nazwisko == temp.nazwisko:
            return True
      return False

class Wypozyczenie():
    def __init__(self, nazwisko, tytul):
        self.nazwisko = str(nazwisko)
        self.tytul = str(tytul)

    def dodaj_wypozyczenie(self, wypozyczenia):
        wypozyczenia.append(Wypozyczenie(self.nazwisko, self.tytul))
    
    def sprawdz_czy_mozna_wypozyczyc_czytelnikowi(nazwisko, wypozyczenia):
        sprawdzarka_wypozyczenTF = True
        licznik_wypozyczen = 0
        for i in range(len(wypozyczenia)):
            wypozyczenie = wypozyczenia[i]
            if wypozyczenie.nazwisko == nazwisko:
                licznik_wypozyczen = licznik_wypozyczen + 1
        if licznik_wypozyczen > 2:
            sprawdzarka_wypozyczenTF = False
        else: 
            sprawdzarka_wypozyczenTF = True
        return sprawdzarka_wypozyczenTF

    def sprawdz_czy_wypozyczono(nazwisko, tytul, wypozyczenia):
        wypTF = False
        for i in range(len(wypozyczenia)):
            wypozyczenie = wypozyczenia[i]
            if wypozyczenie.nazwisko == nazwisko and wypozyczenie.tytul == tytul:
                wypTF = True
        return wypTF
        
    def oddaj_wypozyczenie(nazwisko, tytul, wypozyczenia):
        wypTF = False
        for i in range(len(wypozyczenia)):
            wypozyczenie = wypozyczenia[i]
            if wypozyczenie.nazwisko == nazwisko and wypozyczenie.tytul == tytul:
                wypozyczenie.pop(i)
                wypTF = True
        return wypTF
    
czytelnicy = []
egzemplarze = []
wypozyczenia = []

n=int(input())
for i in range(0, n):
    input_git = input().replace('(', '').replace(')', '').replace(' "', '').replace('"', '').replace('\r', '').replace('\n', '').split(",")
    
    if input_git[0] == "dodaj":
        dodaj = Egzemplarz.dodaj_egzemplarz((Egzemplarz(input_git[1], input_git[2], input_git[3], False)), egzemplarze)
        print(dodaj)
    
    if input_git[0] == "wypozycz":
        wypozyczTF = False
        czy_czytelnik_juz_jest_na_liscie = Czytelnik.sprawdz_czy_czytelnik_jest_na_liscie(czytelnicy, input_git[1])
        if czy_czytelnik_juz_jest_na_liscie == False:
            Czytelnik.dodaj_czytelnika((Czytelnik(input_git[1])), czytelnicy)
        czy_mozna_wypozyczyc_czytelnikowi = Wypozyczenie.sprawdz_czy_mozna_wypozyczyc_czytelnikowi(input_git[1], wypozyczenia)
        if czy_mozna_wypozyczyc_czytelnikowi == True:
            czy_wypozyczono = Wypozyczenie.sprawdz_czy_wypozyczono(input_git[1], input_git[2], wypozyczenia)
            if czy_wypozyczono == False:
                wypozycz_egzemplarz = Egzemplarz.wypozycz_egzemplarz(input_git[2], egzemplarze)
                print(wypozycz_egzemplarz)
                if wypozycz_egzemplarz == True:
                    Wypozyczenie.dodaj_wypozyczenie(Wypozyczenie(input_git[1], input_git[2]), wypozyczenia)
            else:
                print(wypozyczTF)
        else:
            print(wypozyczTF)
    
    if input_git[0] == "oddaj":
        sprawdz_czy_wypozyczono = Wypozyczenie.sprawdz_czy_wypozyczono(input_git[1], input_git[2], wypozyczenia)
        if sprawdz_czy_wypozyczono == False:
            print(sprawdz_czy_wypozyczono)
        else:
            oddaj = Wypozyczenie.oddaj_wypozyczenie(input_git[1], input_git[2], wypozyczenia)
            Egzemplarz.oddaj_egzemplarz(input_git[2], egzemplarze)
            print(oddaj)