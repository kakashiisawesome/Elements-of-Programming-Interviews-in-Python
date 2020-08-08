
def countGoodTriplets(arr, a, b, c):

    count = 0

    for i in range(len(arr) - 2):
        for j in range(i+1, len(arr)-1):
            if abs(arr[i] - arr[j]) > a:
                continue
            for k in range(j+1, len(arr)):
                if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                    print((arr[i], arr[j], arr[k]))
                    count += 1

    return count


countGoodTriplets([1,1,2,2,3], 0,0,1)