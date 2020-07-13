
def quick_sort(l):
    
    # 종료 조건
    if len(l) <= 1:
        return l

    pivot = l[-1]
    g1, g2 = [], []

    for i in range(0, len(l)-1):
        if l[i] < pivot: g1.append(l[i])
        else: g2.append(l[i])

    return quick_sort(g1) + [pivot] + quick_sort(g2)

import random

# init list
size_m_list = 6
m_list = [int(i) for i in range(size_m_list)]
# shuffle list
random.shuffle(m_list)

print(quick_sort(m_list))