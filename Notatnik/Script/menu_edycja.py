import ob_menu_edycja

def rozwin_menu_edycja(): #rozwija menu edycja
  return ob_menu_edycja.ob_menu_edycja().Click()
  
def zwroc_edycja_cofnij(): #zwraca cofnij w menu edycja
  rozwin_menu_edycja()
  return ob_menu_edycja.ob_edycja_cofnij().Click()
  
def zwroc_edycja_kopiuj(): #zwraca kopiuj w menu edycja
  rozwin_menu_edycja()
  return ob_menu_edycja.ob_edycja_kopiuj().Click()
  
def zwroc_edycja_usun(): #zwraca wyczysc w menu edycja
  rozwin_menu_edycja()
  return ob_menu_edycja.ob_edycja_usun().Click()
  
def zwroc_edycja_wklej(): #zwraca wklej w menu edycja
  rozwin_menu_edycja()
  return ob_menu_edycja.ob_edycja_wklej().Click()
  
def zwroc_edycja_zaznacz_wszystko(): #zwraca zaznacz_wszystko w menu edycja
  rozwin_menu_edycja()
  return ob_menu_edycja.ob_edycja_zaznacz_wszystko().Click()
  
