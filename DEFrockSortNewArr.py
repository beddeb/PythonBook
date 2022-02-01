def rockSort(temp):
    x = 1
    while x < len(temp):
        for i in range(len(temp) - x):
            if temp[i] > temp[i + 1]:
                temp[i], temp[i + 1] = temp[i + 1], temp[i]
        x += 1
    return temp