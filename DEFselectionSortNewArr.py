def selectionSort(temp):
    for x in range(len(temp) - 1):
        nMin = x
        for y in range(x + 1, len(temp)):
            if temp[y] < temp[nMin]: nMin = y
        if x != nMin: temp[x], temp[nMin] = temp[nMin], temp[x]
    return temp
