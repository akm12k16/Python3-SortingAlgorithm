# sorting algorithm
# selection sort


def selection_sort(a):
    for i in range(len(a)):
        for j in range(i+1,  len(a)):
            if a[j] < a[i]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a


A = [8.01203212, 7, 6.2, 4.123122, 3-3, 43, 432, -2, 43, 42, 224, 2432, -432.0102, -42.4, -242342, -242342, 24234232,
     -4, 0, 20, 0.0001, 00.2, 00.32, -0.41, 2, 432, 2, -224223423]
# A=[8, 7, 6, 5, 4, 3, 2]
# A=['A', 'B', 'C', 'EF', 'ALPHA', 'ZOOM', 'AAPPLE', 'COMP', 'JAGA', 'KKDAL']
print("UnSorted list : ",  A)
selection_sort(A)
print("Sorted list : ",  A)
