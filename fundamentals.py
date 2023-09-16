lista = ['pikachu','charmander','slowpock','bulbasaur','psyduck','jigglypuff','meowth','diglett']
#print(lista)

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