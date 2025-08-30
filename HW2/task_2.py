AList = [1, 5, 9, 15, 14, 11, 10, 3, 12, 2313, 1325153, 45454]
BList = [2, 4, 5, 3, 15, 11, 2313]
CList = []

for a in AList:
    for b in BList:
        if a == b:
            CList.append(a)

print(CList)