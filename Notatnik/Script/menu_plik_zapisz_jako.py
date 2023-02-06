﻿import ob_plik_zapisz_jako
import menu_plik
import datetime

def wybierz_folder_dokumenty(): #wprowadza sciezke do Dokumenty w oknie Zapisz jako...
  ob_plik_zapisz_jako.ob_sciezka_zapisu().ClickR()
  ob_plik_zapisz_jako.ob_edytuj_sciezka_zapisu().Click()
  ob_plik_zapisz_jako.ob_edyt_sciezka_zapisu().Keys("C:\\Users\\k.ciepieniak\\Documents")
  return Sys.Desktop.Keys("[Enter]")
  
def zwroc_nazwa_pliku(): #klika w pole wprowadzenia nazwy pliku
  return ob_plik_zapisz_jako.ob_nazwa_pliku().Click()
  
def wpisz_nazwe_pliku(x): #wpisuje nazwe pliku
  zwroc_nazwa_pliku()
  data = str(datetime.datetime.now().replace(microsecond=0))
  data = data.replace(":",".")
  ob_plik_zapisz_jako.ob_nazwa_pliku().Keys(x+" "+data)
  return Sys.Desktop.Keys("[Enter]")
  
def zwroc_przycisk_zapisz(): #klika w przycisk zapisz
  return ob_plik_zapisz_jako.ob_przycisk_zapisz().Click()
  
def sprawdz_czy_istnieje_duplikat(): #sprawdz czy w plikach nie znajduje sie duplikat o tej samej nazwie
  p = Sys.Process("notepad++")
  wersja = p.WaitWindow("*", "Potwierdzanie zapisywania jako", -1, 5000)
  if (wersja.Exists):
    return ob_plik_zapisz_jako.ob_przycisk_tak().Click()
  else:
    Log.Message("Brak duplikatu")


  
     
