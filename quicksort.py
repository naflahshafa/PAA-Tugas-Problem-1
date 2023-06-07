def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]


def pivot(list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if list[i] < list[pivot_index]:
            swap_index += 1
            swap(list, swap_index, i)
    swap(list, pivot_index, swap_index)
    return swap_index


def quicksort_helper(list, left, right):
    if left < right:
        pivot_index = pivot(list, left, right)
        quicksort_helper(list, left, pivot_index - 1)
        quicksort_helper(list, pivot_index + 1, right)
    return list


def quicksort(list):
    return quicksort_helper(list, 0, len(list) - 1)


def find_duplicates(list):
    sorted_list = quicksort(list)
    duplicates = []
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] == sorted_list[i + 1] and sorted_list[i] not in duplicates:
            duplicates.append(sorted_list[i])
    return duplicates


list = [4, 1, 7, 3, 8, 16, 4, 9, 2, 8, 12]
duplicate_values = find_duplicates(list)
if duplicate_values:
    print("Data yang duplikat:", duplicate_values)
else:
    print("Tidak ada data yang duplikat")
