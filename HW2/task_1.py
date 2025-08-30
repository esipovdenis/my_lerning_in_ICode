AList = [1, 5, 9, 15, 14, 11, 10, 11, 12, 2313, 1325153, 45454]
BList = [2, 4, 5, 9, 28]
CList = [[[9, 11],10],[5, 4],[6, 7, 9,[3, 5, 7]]]

for list_inside_Clist in CList:
    for list_inside_list_inside_Clist in list_inside_Clist:
        if isinstance(list_inside_list_inside_Clist, list):
         for c in list_inside_list_inside_Clist:
            print(c)
        else:
            print(list_inside_list_inside_Clist)
    print("End")