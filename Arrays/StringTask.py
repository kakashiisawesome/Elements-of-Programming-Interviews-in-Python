

def doTask(s):

    # Get lowercase string
    l = s.lower()
    # Get array from string
    arr = [c for c in l]

    # Delete vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    [arr.remove(i) for i in arr if i in vowels]

    print('After removing :', arr)

    # Insert the  '.'
    i = 0
    while i < len(arr):
        arr.insert(i, '.')
        print(arr, i, len(arr))
        i += 2


    print(''.join(arr))


if __name__ == '__main__':
    s = input()
    doTask(s)
