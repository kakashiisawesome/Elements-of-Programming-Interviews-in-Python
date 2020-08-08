
def destCity(paths):
    couldBe = {}

    for path in paths:
        couldBe[path[0]] = False
        if path[1] not in couldBe:
            couldBe[path[1]] = True

    for k in couldBe:
        if couldBe[k]:
            return k


print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))