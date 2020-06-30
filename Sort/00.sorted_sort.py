import random
import math

# init list
size_m_list = 20
m_list = [int(i) for i in range(size_m_list)]

# shuffle list
random.shuffle(m_list)

print("shuffle list:", end=' ')
print(m_list)

#### Sort #####
m_list = sorted(m_list)
            
print(m_list)
