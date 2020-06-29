import random
import math

# init list
size_m_list = 50
m_list = [int(i) for i in range(size_m_list)]

# shuffle list
random.shuffle(m_list)

print("shuffle list:", end=' ')
print(m_list)

########## Start Sort algorithm ##########
idx = 0; tmp = 0;

for i in range(size_m_list):
    min = math.inf
    for j in range(i, size_m_list):
        if min > m_list[j]:
            min = m_list[j]
            idx = j

    tmp = m_list[i]
    m_list[i] = m_list[idx]
    m_list[idx] = tmp

print(m_list)
