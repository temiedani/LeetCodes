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
def bubbleSort(nums):
    for i in range(len(nums)-1):
        swapped = False
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    nums = [4, 3, 2, 1, 5, 6, 7]
    print(f"Before sorting {nums}")
    bubbleSort(nums)
    print(f"After sorting {nums}")
