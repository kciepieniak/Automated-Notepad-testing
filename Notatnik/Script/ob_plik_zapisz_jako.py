﻿def ob_plik_zapisz_jako(): #zapisz jako...
  return Aliases.notepad_.popupPlik.MenuItem("Zapisz jako...\tCtrl+Alt+S")
  
def  ob_sciezka_zapisu(): #sciezka zapisu
  return Aliases.notepad_.dialogZapisywanieJako.Window("WorkerW", "", 1).Window("ReBarWindow32", "", 1).Window("Address Band Root", "", 1).ProgressBar("Ładowanie").Window("Breadcrumb Parent", "", 1).ToolBar("*")
  
def ob_edyt_sciezka_zapisu(): #sciezka zapisu w edycji
  return Aliases.notepad_.dialogZapisywanieJako.Window("WorkerW", "", 1).Window("ReBarWindow32", "", 1).Window("Address Band Root", "", 1).ProgressBar("Ładowanie").Window("ComboBoxEx32", "", 1).ComboBox("Adres").Edit("Adres")
  
def ob_edytuj_sciezka_zapisu(): #edycja sciezki zapisu
  return Aliases.notepad_.Popup("Kontekst").MenuItem("Edytuj adres")
  
def ob_nazwa_pliku(): #nazwa pliku w oknie Zapisz jako...
  return Aliases.notepad_.dialogZapisywanieJako.panel.Okienko_Eksploratora.panel2.comboboxNazwaPliku.editNazwaPliku

def ob_dialog_o_nadpisaniu(): #dialog czy chcemy nadpisac istniejacy plik
  return Aliases.notepad_.Dialog("Potwierdzanie zapisywania jako")
  
def ob_przycisk_tak(): #przycisk tak w dialogu o nadpisaniu istniejacego pliku
  return Aliases.notepad_.Dialog("Potwierdzanie zapisywania jako").UIAObject("Potwierdzanie_zapisywania_jako").Window("CtrlNotifySink", "", 7).Button("Tak")
