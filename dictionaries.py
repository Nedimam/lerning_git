#create dictionary with countries as keys abd capital cities as values
kraje = {'Polska' : 'Warszawa', 
         'Niemcy' : 'Berlin', 
         'Francja': 'Paryz',
         'Grecja' : 'Atheny',
         'Czechy' : 'Praga'}
print(kraje)


#print in for loop all values
for values in kraje.values():
   print(values)


#print in for loop all keys
for keys in kraje.keys():
   print(keys)


#add two new countries to the dict
kraje.update({'UK': 'London'})
kraje.update({'Norway': 'Oslo'})
kraje["Ukraina"] = "Kijow"
print(kraje)

nowa_lista = ['Polska','Ukraina','Czechy']
print(nowa_lista)


#in for loop print "Capital of {country} is {city}"
stolica_polski = kraje.get('Polska')
print(stolica_polski)

for kraj in nowa_lista:
    print(f"Stolica {kraj} to {kraje.get(kraj)}")
    #print(f"Stolica {kraj} to {kraje[kraj]}")


#add new items to list
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

 
#remove key/val pair from dict
print(kraje)
del kraje['Czechy']
print(kraje)
