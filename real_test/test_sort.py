"""
最好的时间复杂度为：O(nlogn)
最坏的时间复杂度为: O(n²)
平均时间复杂度为：O(nlogn)
"""


def mao_pao(nums):
    for i in range(len(nums) - 1):
        tag = False

        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                tag = True
        if not tag:
            break
    return nums


def quick_sort(nums, start, end):
    if start < end:
        i, j = start, end
        tag = nums[i]
        while i < j:
            while i < j and nums[j] >= tag:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= tag:
                i += 1
            nums[j] = nums[i]
        nums[i] = tag
        quick_sort(nums, start, i - 1)
        quick_sort(nums, j + 1, end)
    return nums


if __name__ == "__main__":
    test_nums = [30, 24, 5, 58, 18, 36, 12, 42, 39]

    print(mao_pao(test_nums))

    start = 0
    end = len(test_nums) - 1
    print(quick_sort(test_nums, start, end))
