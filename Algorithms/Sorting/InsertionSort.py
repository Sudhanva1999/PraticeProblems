a = [2,3,7,9,32,435,757,67,22, 1]

# # Increasing
# i = 1
# while i < len(a):
#     key = a[i]
#     j = i - 1
#     while j >= 0 and a[j] > key:
#         a[j+1] = a[j]
#         j -= 1
#     a[j + 1] = key
#     i += 1

# Decreasing
i = 1
while i < len(a):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] < key:
        a[j+1] = a[j]
        j -= 1
    a[j + 1] = key
    i += 1
print(a)
