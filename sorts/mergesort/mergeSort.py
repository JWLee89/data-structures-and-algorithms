list_test = [2, 38, 35, 23, 1, 9, 82, 13, 15]


def merge(left_list, right_list):
    result_list = []

    # while left and right list has elements
    while left_list and right_list:
        left_list_item = left_list[0]
        right_list_item = right_list[0]

        if left_list_item < right_list_item:
            result_list.append(left_list_item)
            left_list.pop(0)
        else:
            result_list.append(right_list_item)
            right_list.pop(0)

    # empty left list and place items into result list
    while left_list:
        result_list.append(left_list[0])
        left_list.pop(0)

    # empty right list and place items into result list
    while right_list:
        result_list.append(right_list[0])
        right_list.pop(0)

    return result_list

def mergesort(list_of_items):
    list_len = len(list_of_items)

    # base case
    if list_len < 2:
        return list_of_items

    left_list = list_of_items[:list_len // 2]   # //
    right_list = list_of_items[list_len // 2:]  # "//" to force division

    # merge sort left and right list recursively
    left_list = mergesort(left_list)
    right_list = mergesort(right_list)

    return merge(left_list, right_list)

new_list = mergesort(list_test)

for item in new_list:
    print(item)
