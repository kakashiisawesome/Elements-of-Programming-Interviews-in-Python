
from collections import deque

class Employee:
    def __init__(self, id: int, importance: int, subordinates: []):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates



def getImportance(employees, id):
    totalImportance = 0
    emap = {}

    for e in employees:
        if e.id not in emap:
            emap[e.id] = e

    # Search the employee with given id
    target = emap[id]
    # Make a queue
    q = deque()

    # Start with target
    q.append(target)

    while len(q) > 0:
        temp = q.popleft()
        totalImportance += temp.importance
        for s in temp.subordinates:
            q.append(emap[s])

    return totalImportance


if __name__ == '__main__':

    a = Employee(1, 5, [2,3])
    b = Employee(2, 3, [4,])
    c = Employee(3, 3, [5,])
    d = Employee(4, 2, [])
    e = Employee(5, 1, [])

    print(getImportance([a,b,c,d,e], 1))

