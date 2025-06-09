
number_of_test = int(input())

for _ in range(number_of_test):

    element_A = int(input())
    seperate_space_A = set(map(int, input().split()))

    element_B = int(input())
    seperate_space_B = set(map(int, input().split()))

    checking_subset = seperate_space_A.issubset(seperate_space_B)
    
    print(checking_subset)
