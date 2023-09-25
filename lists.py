#create list
lista = ['pikachu','charmander','slowpock','bulbasaur','psyduck','jigglypuff','meowth','diglett']
print(lista)


#using for loop print all elements of the list separated by coma
print(','.join([str(x) for x in range(5)]))
for ele in lista:
    print(','.join([str(ele) for ele in lista]))

string_value = ''
for ele in lista:
    string_value += ele + ','
string_value = string_value[:-1]
print(string_value)


#print all elements that have even idx
even = []
for index, ele in enumerate(lista):
    if index % 2 == 0:
        even.append(ele)
print(even)


#sort list alphabetically
lista.sort()
print(lista)


lista_alf = sorted(lista)
print(lista_alf)


# print list in reversed order
miasta = ['Warszawa', 'Krakow', 'Lodz', 'Bydgoszcz', 'Radom']
miasta.reverse()
print(miasta)


# print prelast element of the list
miasta = ['Warszawa', 'Krakow', 'Lodz', 'Bydgoszcz', 'Radom']
print(miasta[-2])


# print elements that end with z or m
miasta = ['Warszawa', 'Krakow', 'Lodz', 'Bydgoszcz', 'Radom']
for miasto in miasta:   
    if miasto[-1]=='z' or miasto[-1]=='m':
        print(miasto)


# remove elements that have >6 letters
miasta = ['Warszawa', 'Krakow', 'Lodz', 'Bydgoszcz', 'Radom']
for miasto in miasta:
    if len(miasto)>=6:
        miasta.remove(miasto)
print(miasta)


# add to the list another list 
#list1.extend(list2)
male_miasta = ['Pcim','Zabrzerz','Zarzecze']
miasta.extend(male_miasta)
# miasta = miasta + male_miasta
# miasta += male_miasta
print(miasta)

# find idx in the list that is assigned to the first small town name
index = miasta.index('Pcim')
print(index)


# check if item is in the list 
i='Gdansk'
if i in miasta:
    print(True)
else:
    print(False)


# iterate over the list without enumerate
miasta = ['Warszawa', 'Krakow', 'Lodz', 'Bydgoszcz', 'Radom']
for i in range(len(miasta)):
   print(i, '=>', miasta[i])

#assert miasta == ['Krakow', 'Lodz', 'Bydgoszcz'], "test"