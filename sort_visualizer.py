import random


NUMBER_OF_ELEMENTS = 50


def random_nums() -> list:
    nums = []
    randomized_list = []

    for i in range(1, NUMBER_OF_ELEMENTS + 1):
        nums.append(i)

    for j in range(1, NUMBER_OF_ELEMENTS + 1):
        num = random.choice(nums)
        randomized_list.append(num)
        nums.remove(num)

    return randomized_list


def bubble_sort(nums: list) -> list:
    swaps = 0

    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swaps += 1

    print(swaps)
    return nums


def main():
    nums = random_nums()
    print(nums)
    nums = bubble_sort(nums)
    print(nums)


if __name__ == "__main__":
    main()
