
def sortString(s):
    a = sorted(s)
    res = ''
    while len(a) > 0:
        # 1
        last = a.pop(0)
        res += last

        # 2,3
        i = 0
        while i < len(a):
            if a[i] > last:
                last = a[i]
                res = res + a[i]
                a.pop(i)
            else:
                i += 1


        # 4
        if len(a) == 0:
            break

        last = a.pop(len(a)-1)
        res += last

        # 5,6
        i = len(a) - 1
        while i >= 0 and len(a) > 0:
            if a[i] < last:
                res += a[i]
                last = a.pop(i)

            i -= 1



    return res




print(sortString('kwgnfmmfngwk'))

