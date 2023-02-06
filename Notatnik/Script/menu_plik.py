import ob_menu_plik
import ob_plik_nowy
import ob_plik_zakoncz
import ob_plik_zapisz_jako


def rozwin_menu_plik(): #rozwija menu plik
  return ob_menu_plik.ob_menu_plik_edytowany().Click()
  
def zwroc_plik_nowy(): #zwraca nowy w menu plik
  rozwin_menu_plik()
  return ob_plik_nowy.ob_plik_nowy().Click()
  
def zwroc_plik_zakoncz(): #zwraca zakoncz w menu plik
  rozwin_menu_plik()
  return ob_plik_zakoncz.ob_plik_zakoncz().Click()
  
def zwroc_plik_zapisz_jako(): #zwraca zapisz jako
  rozwin_menu_plik()
  return ob_plik_zapisz_jako.ob_plik_zapisz_jako().Click()
  
  

  

  