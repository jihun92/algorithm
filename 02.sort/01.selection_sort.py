import random

def m_sort(lit):
    n = len(lit)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if lit[min_idx] > lit[j]:
                min_idx = j
        lit[i], lit[min_idx] = lit[min_idx], lit[i]

    return lit


# init list
n = 5
m_list = [int(i) for i in range(n)]

# shuffle list
random.shuffle(m_list)

print("shuffle list:", m_list)
print("sort result: ", m_sort(m_list))
