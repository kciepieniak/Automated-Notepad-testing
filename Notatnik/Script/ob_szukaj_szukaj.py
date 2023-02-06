def ob_szukaj_szukaj():
  return Aliases.notepad_.Popup("Szukaj").MenuItem("Szukaj...\tCtrl+F")
  
def ob_znajdz_nastepny():
  return Aliases.notepad_.Dialog("Szukaj").Button("Znajdź następny")
  
def ob_przycisk_zamknij():
  return Aliases.notepad_.Dialog("Szukaj").TitleBar(0).Button("Zamknij")