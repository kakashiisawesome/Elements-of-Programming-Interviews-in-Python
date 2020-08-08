

def shuffle(s, indices):
    s_arr = [c for c in s]
    res = [''] * len(s_arr)

    for i in range(len(s_arr)):
        j = indices[i]
        res[j] = s_arr[i]

    return ''.join(res)



shuffle('aiohn', [3,1,4,2,0])