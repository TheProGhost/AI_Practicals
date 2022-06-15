# String operations

"""

- index
- strip
- count
- split
- upper
- lower
- isupper
- islower
- translate
- formate
- find
- center
- join

"""


str1 = " heLLo, WorLd! "
strL = "äbcd"
strU = "ABCD"
list1 = ['1','2','3','4','5','6','7','8','9']


print("index of the letter \'o\' is",str1.index('o'),end="\n\n")

str2 = str1.strip()
print(str2,end="\n\n")

print("The count of \'L\' is ",str1.count('L'),end="\n\n")

str2 = str1.split()
print(str2,end="\n\n")

print(str1.upper(),end="\n\n")
print(str1.lower(),end="\n\n")

print(strU.isupper(),end="\n\n")
print(strL.islower(),end="\n\n")

table = {104 : 72, 44 : None, 111: 48, 76 : 124 }
print(str1.translate(table),end="\n\n")

x = 12
print("The answer is {}".format(x),end="\n\n")

print("The \'W\' is found at ",str1.find('W'),end="\n\n")

print(str1.center(25,"-"),end="\n\n")

str3 = "_"
str3 = str3.join(list1)

print(str3,end="\n\n")