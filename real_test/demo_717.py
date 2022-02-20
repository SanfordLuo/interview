def demo(bits):
    is_pass = False
    for idx, v in enumerate(bits):
        if is_pass:
            is_pass = False
            continue
        if v == 1:
            is_pass = True
        if idx + 1 == len(bits):
            if v == 0:
                return True
    return False


def test(nums, k):
    ret = 0
    for i, n_i in enumerate(nums):
        tag_nums = nums[i:]
        n_j_a = n_i - k
        n_j_b = n_i + k
        ret += (tag_nums.count(n_j_a) + tag_nums.count(n_j_b))

    return ret


if __name__ == '__main__':
    print(test([1, 2, 2, 1], 1))
