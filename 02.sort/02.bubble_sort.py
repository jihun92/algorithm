import random
import math

# init list
size_m_list = 10
m_list = [int(i) for i in range(size_m_list)]

# shuffle list
random.shuffle(m_list)

print("shuffle list:", end=' ')
print(m_list)

########## Start Sort algorithm ##########
tmp = 0;
for i in range(size_m_list):
    for j in range((size_m_list-1)-i):
        if m_list[j] > m_list[j+1]:
            tmp = m_list[j]
            m_list[j] = m_list[j+1]
            m_list[j+1] = tmp

print(m_list)
