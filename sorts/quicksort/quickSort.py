test_list = [3, 8, 123, 9, 28, 172, 40, 8, 27, 13]


def quicksort(list_of_nums):
    # Base case
    if len(list_of_nums) <= 1:
        return list_of_nums

    pivot = list_of_nums[-1]

    left_list = []

    # Append pivot to right list
    right_list = [pivot]

    for currentItem in list_of_nums[:(len(list_of_nums) - 1)]:
        if currentItem <= pivot:
            left_list.append(currentItem)
        else:
            right_list.append(currentItem)
    # partition the lists and return the concatenated result
    return quicksort(left_list) + quicksort(right_list)


new_list = quicksort(test_list)

for num in new_list:
    print(num)


# Function that is called to run quick sort
def quicksortefficient(list_of_items):
    quicksortimpl(list_of_items, 0, (len(list_of_items) - 1))


# function that runs the partition logic
def partitionlist(list_of_items, low_index, high_index):
    # initialize
    # Change wall_index to low_index
    # and current_index to low_index + 1 to avoid unnecessary swap at the start
    wall_index = low_index - 1
    current_index = low_index

    pivot = list_of_items[high_index]

    for index in range(current_index, high_index):
        current_item = list_of_items[current_index]
        if current_item <= pivot:
            # increment wall index
            wall_index += 1

            # Perform swap with item at wall index and item at currentIndex
            temp = list_of_items[wall_index]
            list_of_items[wall_index] = list_of_items[current_index]
            list_of_items[current_index] = temp

        current_index += 1

    # Lastly, swap pivot with item to the right of the wall
    temp = list_of_items[wall_index + 1]
    list_of_items[wall_index + 1] = list_of_items[high_index]
    list_of_items[current_index] = temp

    return wall_index + 1


# function that recursively calls itself until base case is reached
def quicksortimpl(list_of_items, low_index, high_index):
    if low_index < high_index:
        pivot_index = partitionlist(list_of_items, low_index, high_index)

        quicksortimpl(list_of_items, low_index, pivot_index - 1)
        quicksortimpl(list_of_items, pivot_index + 1, high_index)


print("quick sort efficient ----------")

quicksortefficient(test_list)

for item in test_list:
    print(item)
