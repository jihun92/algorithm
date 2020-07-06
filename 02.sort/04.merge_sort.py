import random

def merge_sort1(l):

    if len(l) <= 1:
        return l

    mid = len(l) // 2
    g1 = merge_sort1(l[:mid])
    g2 = merge_sort1(l[mid:])

    print("group 1: ", l[:mid])
    print("group 2: ", l[mid:])

    rs = []
    while g1 and g2:
        if g1[0] < g2[0]: rs.append(g1.pop(0))
        else:  rs.append(g2.pop(0))

    while g1: rs.append(g1.pop(0))
    while g2: rs.append(g2.pop(0))

    return rs

def merge_sort2(l):

    if len(l) <= 1:
        return

    mid = len(l) // 2
    g1 = l[:mid]
    g2 = l[mid:]
    merge_sort2(g1)
    merge_sort2(g2)

    idx1, idx2, idx_l = 0, 0, 0

    while idx1 < len(g1) and idx2 < len(g2):
        if g1[idx1] < g2[idx2]:
            l[idx_l] = g1[idx1]
            idx1 += 1
            idx_l += 1
        else:
            l[idx_l] = g2[idx2]
            idx2 += 1
            idx_l += 1

    # 남아 있는 자료를 결과에 추가
    for i in range(idx1, len(g1)):
        l[idx_l] = g1[i]
        idx_l += 1

    for i in range(idx2, len(g2)):
        l[idx_l] = g2[i]
        idx_l += 1


# init list
size_m_list = 6
m_list = [int(i) for i in range(size_m_list)]
# shuffle list
random.shuffle(m_list)

# merge_sort1
print(merge_sort1(m_list))

# merge_sort2
merge_sort2(m_list)
print(m_list)