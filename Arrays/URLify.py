

def urlify(s):
    arr = [c for c in s]

    for i in range(len(arr)):
        if arr[i] == ' ':
            arr[i] = '%20'

    res = ''.join(arr)
    print(res)


a = 'Mr John Smith'
urlify(a)
