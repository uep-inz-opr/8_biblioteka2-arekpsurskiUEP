class Ksiazka:
  def __init__(self, tytul, autor):
    self.tytul=str(tytul)
    self.autor=str(autor)

class Egzemplarz:
  wypozyczony = False

  def __init__(self, tytul, autor, rokWydania, wypozyczony):  
    self.tytul=str(tytul)
    self.autor=str(autor)
    self.rokWydania=int(rokWydania)
    self.wypozyczony=bool(wypozyczony)

class Biblioteka:
    ksiazki = []
    egzemplarze = []
    czytelnicy = []

    def __init__(self, limit):
      self.limit=int(limit)

    def dostepni_czytelnicy(self, nazwisko) -> bool:
      self.nazwisko=naziwsko
      czytelnikTF = False
      for czytelnik in self.czytelnicy:
        if czytelnik.nazwisko == nazwisko:
          czytelnikTF = True
      return czytelnikTF
  
    def dostepne_ksiazki(self, tytul, autor)-> bool:
      self.tytul=tytul
      self.autor=autor
      ksiazkaTF = False
      for ksiazka in self.ksiazki:
        if ksiazka.tytul == tytul and ksiazka.autor == autor:
          ksiazkaTF = True
      return ksiazkaTF
  
    def dostepne_egzemplarze(self, tytul)-> bool:
      self.tytul=tytul
      egzTF = False
      for egzemplarz in self.egzemplarze:
        if egzemplarz.tytul == tytul and egzemplarz.wypozyczony == False:
          egzTF = True
      return egzTF

    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rokWydania):
          ksiazka = self.dostepne_egzemplarze(tytul)
          if ksiazka == False:
              ksiazka = Ksiazka(tytul, autor)
              self.ksiazki.append(ksiazka)
          self.egzemplarze.append(Egzemplarz(tytul, autor, rokWydania))

    def wypozycz_biblioteka(self, nazwisko, tytul)->bool:
      czytelnik = self.dostepni_czytelnicy(nazwisko)
      if czytelnik == False:
        czytelnik = Czytelnik(nazwisko)
        self.czytelnicy.append(czytelnik)
      if(len(czytelnik.wypozyczenia) >= 3):
        return False
      if(czytelnik.dostepne_egzemplarze(tytul) == True):
        return False
      egzemplarz = self.dostepne_egzemplarze(tytul)
      if(egzemplarz != True):
        return False
      egzemplarz.wypozycozny == True
      czytelnik.wypozycz(egzemplarz)
      return True

    def oddaj_biblioteka(self, nazwisko, tytul)->bool:
      czytelnik = self.dostepni_czytelnicy(nazwisko)
      if(czytelnik != True):
        return False
      egzemplarz = czytelnik.dostepne_egzemplarze(tytul)
      if(egzemplarz != True):
        return False
      egzemplarz.wypozyczony == False
      czytelnik.oddaj(tytul)
      return True

class Czytelnik:
  wypozyczenia = []
  def __init__(self, nazwisko):
    self.nazwisko=str(nazwisko)

  def wypozycz_czytelnik(self, tytul, autor, rokWydania)->bool:
    egzemplarz = Egzemplarz(tytul, autor, rokWydania)
    self.wypozyczenia.append(egzemplarz)
    return True

  def oddaj_czytelnik(self, tytul)->bool:
    wypozyczenia_lista = self.wypozyczenia
    for egzemplarz in wypozyczenia_lista:
      if egzemplarz.tytul == tytul and egzemplarz.autor == autor:
        self.wypozyczenia.remove(egzemplarz)
      if(len(wypozyczenia_lista) == len(self.wypozyczenia)):
        return False
    return True

biblioteka=Biblioteka(3)
czytelnik=Czytelnik()
pozycje=[]
n=int(input())
for i in range (0,n):
  input_git = input().replace('(', '').replace(')', '').replace(' "', '').replace('"', '').replace('\r', '').replace('\n', '').split(",")
  if input_git[0] == 'dodaj':
      dodaj = biblioteka.dodaj_egzemplarz_ksiazki(input_git[1], input_git[2], input_git[3])
      print(dodaj)
  wypozyczenie = True    
  if input_git[0] == 'wypozycz':
      wypozycz_biblioteka = biblioteka.wypozycz_biblioteka(input_git[1], input_git[2])
      wypozycz_czytelnik = czytelnik.wypozycz_czytelnik(input_git[1], input_git[2], input_git[3])
      if wypozycz_biblioteka == wypozycz_czytelnik:
        print(wypozyczenie)
      else:
        wypozyczenie = False
        print(wypozyczenie)
  oddanie = True
  if input_git[0] == 'oddaj':
      oddaj_biblioteka = biblioteka.oddaj_biblioteka(input_git[1], input_git[2])
      oddaj_czytelnik = czytelnik.oddaj_czytelnik(input_git[1])
      if oddaj_biblioteka == oddaj_czytelnik:
        print(oddanie)
      else:
        oddanie = False
        print(oddanie)
