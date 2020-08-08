
def canBeEqual(target, arr):

    if sorted(arr) != sorted(target):
        return False


    for i in range(len(target)):
        for j in range(i, len(arr)):
            if arr[j] == target[i]:
                if i == 0:
                    arr[i:j+1] = arr[j::-1]
                else:
                    arr[i:j + 1] = arr[j:i - 1:-1]
                if arr == target:
                    return True
                break

    return False





a = [1, 1,1,1]
print(canBeEqual(a, [1,1,1,1]))