def sort(list):
    for j in range(1, len(list), 1):
        for i in range(len(list)-j):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list
