
def flip(arr, index):
    for i in range(index, len(arr)):
        if arr[i] == '0':
            arr[i] = '1'
        else:
            arr[i] = '0'


def minFlips(str):
    res = ['0']*len(str)
    count = 0

    for i in range(len(str)):
        if str == ''.join(res):
            break
        if str[i] != res[i]:
            flip(res, i)
            count += 1

    return count


minFlips('001011101')