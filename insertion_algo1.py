# sorting algorithm
# insertion sorting


def insertion_sort(a):
    for i in range(1, len(a)):
        print("In the i {%s} A : {%s}" % (i, a))
        key = a[i]
        j = i - 1
        print('Before entering in the while j : {%s}  , i : {%s}  , key : {%s}' % (j, i, key))
        while j >= 0 and a[j] > key:
            print("In the j {%s} A : {%s}" % (j, a))
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key

        # for j in range(i-1, 0):
        #     print('j for loop', j)
        #     if a[j] > a[i]:
        #         print("In the j {%s} i {%s} A : {%s}" % (j, i, a))
        #         temp = a[j]
        #         a[j] = a[j+1]
        #         a[j+1] = temp
        #         print("In the j {%s} i {%s} A : {%s}" % (j, i, a))
    return a


# A = [8.01203212, 7, 6.2, 4.123122, 3-3, 43, 432, -2, 43, 42, 224, 2432, -432.0102, -42.4, -242342, -242342, 24234232,
# 4, 0, 20, 0.0001, 00.2, 00.32, -0.41, 2, 432, 2, -224223423]
# A = [4, 3, 8, 7, 6, 5, 4, 3, 2]
A = [5, 4, 6, 8, 1]
# A = ['KA', 'CB', 'EC', 'EF', 'ALPHA', 'ZOOM', 'D', 'J']
print("UnSorted list : ", A)
insertion_sort(A)
print("Sorted list : ", A)
j = range(len(A), 0)
print(j)
j = range(len(A))
print(j)
