def ob_menu_edycja():
 # return Aliases.notepad_.formNowy1Notepad.MenuBar("Aplikacja").MenuItem("Edycja")
  return Aliases.notepad_.formNowy1Notepad.menubarAplikacja.MenuItem("Edycja")
  
def skrot_edycja():
  return Aliases.notepad_.Popup("Edycja")

def ob_edycja_cofnij():
  return skrot_edycja().MenuItem("Cofnij\tCtrl+Z or Alt+Backspace")
  
def ob_edycja_kopiuj():
  return skrot_edycja().MenuItem("Kopiuj\tCtrl+C or Ctrl+INS")
  
def ob_edycja_wklej():
  return skrot_edycja().MenuItem("Wklej\tCtrl+V or Shift+INS")

def ob_edycja_usun():
  return skrot_edycja().MenuItem("Wyczyść\tDEL")
  
def ob_edycja_zaznacz_wszystko():
  return skrot_edycja().MenuItem("Zaznacz wszystko\tCtrl+A")
 