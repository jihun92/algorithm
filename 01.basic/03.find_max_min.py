def find_max(a):
    n = len(a)
    max_v = 0
    for i in range(n):
        if a[i] > max_v: max_v = a[i]
    return max_v

def find_min(a):
    n = len(a)
    min_v = a[0]
    for i in range(n):
        if a[i] < min_v: min_v = a[i]
    return min_v

def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(n):
        if a[i] > a[max_idx]: max_idx = i
    return max_idx

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(n):
        if a[i] < a[min_idx]: min_idx = i
    return min_idx

# main
arr = [10,1,13,5,6,2,7,8]
print("max value: %d" %find_max(arr))
print("max idx: %d" %find_max_idx(arr))
print("min value: %d" %find_min(arr))
print("min idx: %d" %find_min_idx(arr))
