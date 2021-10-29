def funkcja(list1, list2):
    list3 = []
    for i in list1:
        if i % 2 == 0:
            list3.append(i)
    for i in list2:
        if i % 2 == 0:
            list3.append(i)
    print(list3)


list1 = [4, 6, 2, 3, 5, 7, 8, 9]
list2 = [7, 2, 4, 6, 8, 9, 2]
funkcja(list1, list2)2