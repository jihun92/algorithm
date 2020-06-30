
def sum_n(n):
    rs = 0
    for i in range(1, n+1):
        rs += i
    return rs

def sum_squre(n):
    rs = 0
    for i in range(1, n+1):
        rs += i**2
    return rs

# main
print("sum_n result: %d" %sum_n(10))
print("sum_n result: %d" %sum_n(100))
print("sum_squre result: %d" %sum_squre(10))
