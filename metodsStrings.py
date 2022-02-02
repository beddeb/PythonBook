#Методы строк
s1, s2 = 'qwerty', "0123"

print("q" in s1, "q" in s2)    #True False

print("q" not in s1, "q" not in s2)    #False True

print(s1 + "123")   #"qwerty123"

print(s1 * 3)   #"qwertyqwertyqwerty"

print(s1[4], s1[2])    #"t" "e"

print(s1[2:5])  #"ert"

print(len(s1), len(s2))    #6 4

print(s1.find("er"), s2.find("er"))    #2 -1

print(s1.rfind("er"), s2.rfind("er"))   #2 -1

print(s1.count("rt"), s2.count("rt"))    #1 0

print(s1.startswith("we"), s1.startswith("qw"))    #False True

print(s2.endswith("3"), s2.endswith("1"))   #True False

print(s1.isdigit(), s2.isdigit())   #False True

print(s1.isalpha(), s2.isalpha())   #True False

print(s1.isalnum(), "E315".isalnum())   #True True

print(s1.islower(), s1.isupper())   #True False

print(s1.upper(), "QWERTY".upper())    #"QWERTY" "QWERTY"
s1 = 'qwerty'

print(s1.lower(), "QWERTY".lower())    #"qwerty" "qwerty"
s1 = 'qwerty'

print(s1.capitalize())     #"Qwerty"
s1 = 'qwerty'

print(' ' + s1 + ' '.lstrip())     #" qwerty"
print(' ' + s1 + ' '.rstrip())     #"qwerty "
print(' ' + s1 + ' '.strip())   #"qwerty"

print(s1.ljust(8, "!"))    #qwerty!!
print(s1.rjust(8, "!"))    #"!!qwerty"

print('+'.join(["qw", "er", "ty"]))    #"qw+er+ty"

print("qw+er+ty".split('+'))    #['qw', 'er', 'ty']

print(s1.replace("qw", "ty"))   #"tyerty"
print(s1.replace("ty", "qw"))   #"qwerqw"

print(list(s1))    #['q', 'w', 'e', 'r', 't', 'y']

print(int(s2))  #123

print(float(s2)) #123.0

print(str(25))  #"25"
