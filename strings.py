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