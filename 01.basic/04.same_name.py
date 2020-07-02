
def find_same_name(a):
    n = len(a)
    rs = set()
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                rs.add(a[i])
    return rs

def couple(a):
    n = len(a)
    rs = set()
    for i in range(n):
        for j in range(n):
            if a[i] != a[j]:
                rs.add("%s - %s" %(a[i], a[j]))
    return rs


# main
arr = ["Mark", "Tom", "Luke", "David", "Mark", "Tom", "John", "Mark" ]
#arr = ["Mark", "Tom", "Luke", "Mark"]
print(find_same_name(arr))
print(couple(arr))
