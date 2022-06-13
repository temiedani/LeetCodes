import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

#  Time-log(n)


@time_it
def binarySearch(nums, target):
    left_index = 0
    right_index = len(nums)-1
    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        if target == nums[mid_index]:
            return mid_index
        elif target < nums[mid_index]:
            right_index = mid_index-1
        elif target > nums[mid_index]:
            left_index = mid_index+1
    return -1

# no loops


# @time_it
def binarySearch_recursive(nums, target, left_index, right_index):
    if right_index < left_index:
        return -1
    mid_index = (left_index+right_index)//2
    if target == nums[mid_index]:
        return mid_index
    elif target < nums[mid_index]:
        right_index = mid_index-1
    elif target > nums[mid_index]:
        left_index = mid_index+1
    return binarySearch_recursive(nums, target, left_index, right_index)


def find_all_occurances(numbers, number_to_find):
    index = binarySearch(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 11, 11, 17, 19, 23, 55]
    print(binarySearch(nums, 11))
    print(binarySearch_recursive(nums, 11, 0, len(nums)))
    print(find_all_occurances(nums, 11))
