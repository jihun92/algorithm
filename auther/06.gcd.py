def gcd(a,b):
    for i in range(min(a,b), 0, -1):
        if a%i==0 and b%i==0:
            return i

def euclid_gcd(a, b):
    if  b == 0:
        return a
    return  euclid_gcd(b,a%b)

# main
print("gcd:")
print(gcd(1,5)) # 1
print(gcd(60,24)) # 12
print(gcd(81,27)) # 27

print("euclid_gcd:")
print(euclid_gcd(1,5)) # 1
print(euclid_gcd(60,24)) # 12
print(euclid_gcd(81,27)) # 27
