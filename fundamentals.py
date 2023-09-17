lista = ['pikachu','charmander','slowpock','bulbasaur','psyduck','jigglypuff','meowth','diglett']
print(lista)

#wypisz w petli for wszystkie elementy z listy po przecinku
print(','.join([str(x) for x in range(5)]))

for ele in lista:
    print(','.join([str(ele) for ele in lista]))


string_value = ''
for ele in lista:
    string_value += ele + ','
string_value = string_value[:-1]
print(string_value)

#wszystkie elementy, ktore maja index parzysty

even = []
for index, ele in enumerate(lista):
    if index % 2 == 0:
        even.append(ele)
print(even)

#wypisz posortowana liste alfab.
lista.sort()
print(lista)

lista_alf = sorted(lista)
print(lista_alf)

#slownik, 5 krajow eu jako klucze, solicy - value

kraje = {'Polska' : 'Warszawa', 
         'Niemcy' : 'Berlin', 
         'Francja': 'Paryz',
         'Grecja' : 'Atheny',
         'Czechy' : 'Praga'}
print(kraje)

#wypisz w petli for, wszystkie wartosci
for values in kraje.values():
   print(values)

#wypisz w petli for, wszystkie klucze
for keys in kraje.keys():
   print(keys)


#   add two new countries to the dict

kraje.update({'UK': 'London'})
kraje.update({'Norway': 'Oslo'})
kraje["Ukraina"] = "Kijow"
print(kraje)

nowa_lista = ['Polska','Ukraina','Czechy']
print(nowa_lista)

# Wypisz w petli for Stolica x jest y

stolica_polski = kraje.get('Polska')
print(stolica_polski)

for kraj in nowa_lista:
    print(f"Stolica {kraj} to {kraje.get(kraj)}")
    #print(f"Stolica {kraj} to {kraje[kraj]}")


# add new items to list
nowa_lista.append("Kolumbia")
nowa_lista.append("Meksyk")
print(nowa_lista)

for ele in nowa_lista:
    if ele in kraje.keys():
        print(True)
    else:
        print(False)

#remove item form list
nowa_lista.remove("Czechy")
print(nowa_lista)

# remove key/val pair from dict
print(kraje)
del kraje['Czechy']
print(kraje)