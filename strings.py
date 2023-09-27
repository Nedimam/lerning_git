string_one = "salatka grecka"
string_two = "salatka chlopska"

#in for loop print every third character
result = string_one[1::2]
print(result)


for index, ele in enumerate(string_one):
    if index %3 == 0:
        print(index,ele)

#print string in reversed order
rever = string_one[::-1]
print(rever)

#print two strings
print(string_one,string_two)

#combine two strings
new_str = string_one+" "+string_two
print(new_str)

#print len(str)
print(len(string_one))

#print the longer string
if len(string_one)>len(string_two):
    print(string_one)
else:
    print(string_two)

#print number of occurences of letter "a"
count = 0
for char in string_one:
    if char == "a":
        count+=1
print(count)

#print string all in caps lock
print(string_one.upper())

#print string in lower
print(string_two.lower())

#check if string starts with some word
print(string_one.startswith('salatka'))

#check if string ends with some word
print(string_one.endswith('grecka'))

#split string to get a list of words
print(string_one.split(' '))

#print all letters of a string starting with third 
print(string_one[3:])

#change string to a list of letters
str_list = ([*string_one])

#change one letter of a list from string
str_list[6] = 'i'
x = "".join(str_list)
print(x)

#use capitalise
print(string_one.capitalize())