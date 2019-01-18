# sorting algorithms
# mergeSort


def merge_sort(a):
    n = len(a)
    if n < 2:
        return a
    q = int(n / 2)
    left = a[:q]
    right = a[q:]
    # print("left : {%s} ,  right : {%s},  A : {%s}" % (left, right, a))
    merge_sort(left)
    merge_sort(right)
    a = merge(a, left, right)
    # print("Result A ", a)
    return a


def merge(a, left, right):
    l = len(left)
    r = len(right)
    i, j, k = 0, 0, 0
    # print("In merge function left : {%s} ,  right : {%s},  A : {%s}" % (left, right, a))
    while i < l and j < r:
        if left[i] <= right[j]:
            a[k] = left[i]
            k = k + 1
            i = i + 1
        else:
            a[k] = right[j]
            k = k + 1
            j = j + 1
    while i < l:
        a[k] = left[i]
        k = k + 1
        i = i + 1
    while j < r:
        a[k] = right[j]
        k = k + 1
        j = j + 1
    return a


# A=[8.01203212, 7, 6.2, 4.123122, 3-3, 43, 432, -2, 43, 42, 224, 2432, -432.0102, -42.4, -242342, -242342, 24234232,
# -4, 0, 20, 0.0001, 00.2, 00.32, -0.41, 2, 432, 2, -224223423]
A = ['A', 'B', 'C', 'EF', 'ALPHA', 'ZOOM', 'AAPPLE', 'COMP', 'JAGA', 'KKDAL']
# A = [8, 7, 6, 3, 9, -2, 19, 21, -2]
print("UnSorted list : ", A)
merge_sort(A)
print("Sorted list : ", A)
