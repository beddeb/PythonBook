def bubbleSort(temp):
    for x in range(len(temp) - 1):
        for y in range(len(temp) - 2, x - 1, -1):
            if temp[y + 1] < temp[y]: temp[y], temp[y + 1] = temp[y + 1], temp[y]
    return temp