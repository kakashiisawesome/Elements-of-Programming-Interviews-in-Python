# Implement an algorithm that takes as input an array of distinct elements and a size, and returns
# a subset of the given size of the array elements. All subsets should be equally likely. Retum the
# result in input array itself.
import random

def random_sampling(A, k):
    for i in range(k):
        # Generate a random index from i to len(A) - 1 and swap A[i] with it
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]


