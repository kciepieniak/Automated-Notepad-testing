import zwroc_tekst_glowny

def wpisz_tekst_glowny(): #wprowadza tekst w oknie glownym
  zwroc_tekst_glowny.zwroc_tekst_glowny()
  return Aliases.notepad_.formNowy1Notepad.panel.Keys('Oto przykladowy tekst dla potrzeb testu automatycznego.')
  
def podmien_tekst_glowny(): #podmienia tekst w oknie glownym
  return Aliases.notepad_.formNowy1Notepad.panel.Keys('podmieniony')