# A items are to be delivered in a circle of size B.
# Find the position where the Ath item will be delivered
#  if we start from a given position C.
# NOTE: Items are distributed at adjacent positions 
# starting from C.

def solve(A, B, C):
        if(C > B):
            C = C % B
        if(((A % B) + C) > B):
            return  ((A % B) + C) - B - 1 
        else:
            return ((A % B) + C) - 1

print(solve(2, 5, 1))