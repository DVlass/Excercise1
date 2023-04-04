a_list = [12, 10, 14, 14, 16, 28, 28, 30]

print("The list is:", a_list)

def removeDuplicates(duplist):
        noduplist = []

        for item in duplist:
            if item not in noduplist:
                noduplist.append(item)
        
        return noduplist

print("The new list without duplicates is:", removeDuplicates(a_list))


def sortList(a_list):

    for i in range(0, len(a_list)):
        for j in range(i+1, len(a_list)):
             if (a_list[i] > a_list[j]):
                temp = a_list[i]
                a_list[i] = a_list[j]
                a_list[j] = temp
    return a_list

print("The sorted list in ascending order is:", sortList(a_list))
