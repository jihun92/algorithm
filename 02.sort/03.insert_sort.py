import random
import math

def insert_sort(lit):

    for i in range(1, len(lit)):
        key = lit[i]
        j = i-1
        while j > -1 and lit[j] > key:
            lit[j+1] = lit[j]
            j -= 1
        lit[j+1] = key
            
    return lit


# init list
size_m_list = 10
m_list = [int(i) for i in range(size_m_list)]

# shuffle list
random.shuffle(m_list)

print("shuffle list:", m_list)
print("sort result:", insert_sort(m_list))
