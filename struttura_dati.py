
"""
## Legenda:
  - ordinato: gli elementi hanno un ordine definito.
  - indicizzato: gli elementi hanno un indice numerico.
  - modificabile: è possibile modificare ( tipo aggiungere, modificare, rimuovere) gli elementi dopo la creazione.
  - immutabile: non è possibile modificare gli elementi dopo la creazione.
  - premette duplicati: è possibile avere più elementi con lo stesso valore.

## Tipi di strutture dati:
- Le liste sono collezioni ordinate e modificabili di elementi. Permettono duplicati.
- Le tuple sono collezioni ordinate e immutabili di elementi. Permettono duplicati.
- I set sono collezioni non ordinate e non indicizzate di elementi. Non permettono duplicati.
- I dizionari sono collezioni ordinate* e modificabili (dalla versione 3.7) di elementi. Non permettono duplicati.
"""
list_data = ["Bari", "Milano", "Torino"] # lista
tuple_data = ("Bari", "Milano", "Torino") # tupla
set_data = {"Bari", "Milano", "Torino"} # set
dict_data = {"Bari": 1, "Milano": 2, "Torino": 3} # dizionario

def typeData(lista_di_data):
  if type(lista_di_data) is list:
    return "LIST\n"
  elif type(lista_di_data) is tuple:
    return "TUPLE\n"
  elif type(lista_di_data) is set:
    return "SET\n"
  else:
    return "DICT\n"

def readData(lista_di_data):
  print(typeData(lista_di_data))
  for data in lista_di_data:
    print(data)
  else:
    print("End of data\n")

readData(list_data)
readData(tuple_data)
readData(set_data)
readData(dict_data)
