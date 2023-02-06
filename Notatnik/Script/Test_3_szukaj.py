import menu_szukaj
import uruchom_zamknij
import menu_szukaj_szukaj
import wpisz_tekst_glowny

def szukaj_frazy():
  uruchom_zamknij.uruchom()                    #uruchamia aplikacje
  wpisz_tekst_glowny.wpisz_tekst_glowny()      #wpisuje tekst w oknie glownym 
  menu_szukaj_szukaj.zwroc_znajdz_nastepny()   #wpisuje fraze w szukaj

  