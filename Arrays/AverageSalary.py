
def average(salary):
    salary.sort()
    sum = 0
    for i in range(1, len(salary)-1):
        sum += salary[i]

    ave = sum/(len(salary)-2)
    return ave


print(average([8000,9000,2000,3000,6000,1000]))