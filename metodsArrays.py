#Методы списков
s1, s2 = [i for i in range(4)], [i for i in range(4, 16 + 1)]

print(3 in s1, 17 in s1)   #True False

print(3 not in s1, 17 not in s1)   #False True

print(s1 + s2)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(3 * s1)   #[0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]

print(s1[3], s1[2], s1[1], s1[0])   #3 2 1 0

print(s1[1:3])  #[1, 2]

print(len(s1))  #4

print(max(s1))  #3

print(min(s1))  #0

print(sum(s1))  #6

print(s1.index(3), s2.index(15))    #3 11

print(s1.count(3), s2.count(3))    #1 0

temp = s1.append(7)   # <=> s1 + [7]; [0, 1, 2, 3, 7]
s1 = [i for i in range(4)]

temp = s1.extend(s2)   # <=> s1 + s2; [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
s1 = [i for i in range(4)]

del s1[2]   #[0, 1, 3]
s1 = [i for i in range(4)]

del s1[1:3]    #[0, 3]
s1 = [i for i in range(4)]

s1.clear()     #[]
s1 = [i for i in range(4)]

temp = s1.copy()    #[0, 1, 2, 3]

s1.insert(0, -1)    #[-1, 0, 1, 2, 3]
s1.insert(5, -1)    #[-1, 0, 1, 2, 3, -1]
s1 = [i for i in range(4)]

temp = s2.pop(6)    #10
print(temp, s2)    #10 [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
s2 = [i for i in range(4, 16 + 1)]

s2.remove(7) #[4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]
s2 = [i for i in range(4, 16 + 1)]

temp = [2, 1, 3, 0]
temp.sort()    #[0, 1, 2, 3]
temp.sort(reverse=True)    #[3, 2, 1, 0]

print(bool([1]))    #True
print(bool([]))    #False