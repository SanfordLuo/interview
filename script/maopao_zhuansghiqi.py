import time
def func1(fun):
    def func2(nums):
        begin_time = time.time()
        fun(nums)
        end_time = time.time()
        print("所花时间：%s" % (end_time - begin_time))
    return func2

@func1
def main(nums):
    for i in range(len(nums) - 1):  # 设置冒泡排序进行的次数
        for j in range(len(nums) - i - 1):  # ｊ为列表下标
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(nums)

nums = [5, 2, 45, 6, 8, 2, 1]
main(nums)
