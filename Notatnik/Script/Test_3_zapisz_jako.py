import uruchom_zamknij
import menu_plik
import menu_plik_zapisz_jako
import wpisz_tekst_glowny

def operacje_na_tekscie():
  uruchom_zamknij.uruchom()                    #uruchamia aplikacje
  wpisz_tekst_glowny.wpisz_tekst_glowny()      #wpisuje tekst w oknie glownym 
  menu_plik.zwroc_plik_zapisz_jako()           #zwraca zapisz jako...
  menu_plik_zapisz_jako.wybierz_folder_dokumenty() #wpisuje sciezke do folderu dokumenty
  menu_plik_zapisz_jako.wpisz_nazwe_pliku("nazwa_pliku")    #klika w box nazwy pliku, wpisuje nazwe i zatwierdza
  menu_plik_zapisz_jako.sprawdz_czy_istnieje_duplikat() #sprawdz czy istnieje duplikat nazwy
  