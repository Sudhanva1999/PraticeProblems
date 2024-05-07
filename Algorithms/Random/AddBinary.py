
a = [1,1,0,0,0,0,0,0]
b = [1,0,0,0,0,0,0,0]
c = [0,0,0,0,0,0,0,0,0]
i = 0
carry = 0
while i < len(a):

    sum = a[i] + b[i] + carry
    carry = sum // 2
    c[i] = sum % 2
    i += 1
c[i] = carry

print(c)

