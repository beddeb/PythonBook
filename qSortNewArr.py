import random

def quicksort(temp):
    if len(temp) <= 1: return temp
    else: qwerty = random.choice(temp)
    x_arr = [i for i in temp if i < qwerty]
    y_arr = [qwerty] * temp.count(qwerty)
    z_arr = [n for n in temp if n > qwerty]
    return quicksort(x_arr) + y_arr + quicksort(z_arr)
