# Your input is an array of integers, and you have to reorder its entries
# so that the even entries appear first
import bisect

def evenOdd(arr):
    nextEven, nextOdd = 0, len(arr)-1
    while nextEven < nextOdd:
        # If we find an odd number
        if arr[nextEven] % 2 != 0:
            # Swap with nextOdd position
            arr[nextEven], arr[nextOdd] = arr[nextOdd], arr[nextEven]
            nextOdd -= 1
        else:
            # Continue iterating
            nextEven += 1


if __name__ == '__main__':
    a = [1,13,12,7,2,5,181,14]
    b = a[:]
    b[0] = 'oo'
    # evenOdd(a)
    print(b)

    

