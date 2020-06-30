import random
import math

# init list
size_m_list = 20
m_list = [int(i) for i in range(size_m_list)]

# shuffle list
random.shuffle(m_list)

print("shuffle list:", end=' ')
print(m_list)

########## Start Sort algorithm ##########
for i in range(1, len(m_list)):
    for j in range(i, 0, -1):
        if m_list[j-1] > m_list[j]:
            m_list[j], m_list[j-1] = m_list[j-1], m_list[j]
            
print(m_list)
