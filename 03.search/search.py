def search_list(x, a):
    n = len(a)
    find_v = []
    for i in range(n):
        if a[i] == x: find_v.append(i)
    return find_v

def search_student(x , lit_no, lit_n):
    n = len(lit_n)

    for i in range(n):
        if lit_no[i] == x: return lit_n[i]
    return -1

# main
m_list = [26, 45 ,26 ,46 ,32, 12, 124, 43, 32, 74, ]
print(search_list(32, m_list))
print(search_list(45, m_list))
print(search_list(111, m_list))

stu_no = [39, 14, 67, 105]
stu_name = ["John", "Mark", "Luke", "David"]
print(search_student(67, stu_no, stu_name))
