import random

def selectionSort(temp):
    cout = 0
    for x in range(len(temp) - 1):
        nMin = x
        for y in range(x + 1, len(temp)):
            if temp[y] < temp[nMin]: nMin = y
        if x != nMin: temp[x], temp[nMin] = temp[nMin], temp[x]; cout += 1
    return temp, cout

def bubbleSort(temp):
    cout = 0
    for x in range(len(temp) - 1):
        for y in range(len(temp) - 2, x - 1, -1):
            if temp[y + 1] < temp[y]: temp[y], temp[y + 1] = temp[y + 1], temp[y]; cout += 1
    return temp, cout

f1 = [random.randint(1, 10000) for _ in range(1000)]
f2 = f1.copy()
print(f'Base() ArrLen: {len(f1)}')
print(f'selectionSort() ArrChanges: {selectionSort(f1)[1]}')
print(f'bubbleSort() ArrChanges: {bubbleSort(f2)[1]}')

