A = int(input())
separate_A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    op_info = input().split()
    operation = op_info[0]
    other_set = set(map(int, input().split()))

    # Perform the mutation
    getattr(separate_A, operation)(other_set)

# Final result
print(sum(separate_A))