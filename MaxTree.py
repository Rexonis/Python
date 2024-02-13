N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()
if A[0] >= 0 or A[-1] <= 0:
    max_product = A[-3] * A[-2] * A[-1]
else:
    max_product = max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
print(max_product)
