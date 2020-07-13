import random

# init list
size_m_list = 20
m_list = [int(i) for i in range(size_m_list)]

# shuffle list
random.shuffle(m_list)
print("shuffle list:", m_list)

#### Sort 1 #####
m_list = sorted(m_list)
print(m_list)

# shuffle list
random.shuffle(m_list)
print("shuffle list:", m_list)

#### Sort 2 #####
m_list.sort()
print(m_list)
