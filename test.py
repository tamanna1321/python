#WAP TO REVERSE A STRING
a="World"
reverse= a[::-1]
print(reverse)

#WAP TO CHECK THE STRING IF ITS PALINDROME OR NOT
b="radar"
is_palindrome=b==b[::-1]
print(is_palindrome)

#WAP TO COUNT THE NUMBER OF VOWELS IN A STRING
c="Tamanna"
vowels="a,e,i,o,u,A,I,E,O,U"
count=sum (1 for char in c if char in vowels)
print(count)

#WAP TO REMOVE ALL WHITESPACES FORM A STRING
d=" Python Language "
no_whitespaces="".join(d.split())
print(no_whitespaces)

#WAP TO SWAP CASES IN A STRING
e="Python Language"
swap_case=e.swapcase()
print(swap_case)

#WAP TO FIND MOST FREQUENT WORD IN A GIVEN STRING
f=["Python is a programming language","Python is OOP'S based","Python is case sensitive language","Python is easy"]



#WAP TO CHECK IF A STRING IS AN ANAGRAM OF ANOTHER STRING
g1="song"
g2="music"
is_anagram= sorted(g1)==sorted(g2)
print(is_anagram)

#WAP TO CONVERT A STRING TO CAMEL CASE
h="Python Language"
camel_case=""
capitalize_next=False
for char in h:
    if char =='_':
        capitalize_next=True
    elif capitalize_next:
        camel_case +=char.upper()
        capitalize_next=False
    else:
        camel_case +=char
        print(camel_case)



#WAP TO CHECK IF A STRING CONTAINS ONLY DIGITS
i ="123456"
digit=i.isdigit()
print(digit)



