def find_lcs_sorted_arrays(arr1, arr2):
    lcs = []
    i = 0
    j = 0
    n1 = len(arr1)
    n2 = len(arr2)

    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            lcs.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return lcs