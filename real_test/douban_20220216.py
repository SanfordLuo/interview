"""
豆瓣 20220216
1、在显示外国作者姓名时，豆瓣会按照惯例展示国籍，如 [奥] 卡夫卡，[日] 村上春树 等。用户添加作者数据时使用括号可能不规范或不匹配，如【德】，惠特曼[美]，[英]等；也可能有多国籍的作者，如 [美][加]。假设括号类型只有四种：()，[]，【】,〔〕，请使用你熟悉的编程语言将国籍信息从作者姓名字符串中去除，考虑前述及其他可能的特殊情况。
3、假设字符串仅由英文单词组成，写一个程序颠倒其中单词的顺序，如“fine by me”处理后变为“me by fine”。但量词（a/an/the）后面如果跟随了一个非量词，那么这两个词应看做一个完整的单词，如“this is a pen on the desk but a an”，处理后应为：“an a but the desk on a pen is this”。请附上你的程序时间复杂度及测试用例
5、You are given a set of numbers 0-n.Given a k,print all subsets of size k.
"""
import itertools


def check_name(name_str):
    if '(' in name_str:
        idx_a, idx_b = name_str.index('('), name_str.index(')')
    elif '[' in name_str:
        idx_a, idx_b = name_str.index('['), name_str.index(']')
    elif '【' in name_str:
        idx_a, idx_b = name_str.index('【'), name_str.index('】')
    elif '〔' in name_str:
        idx_a, idx_b = name_str.index('〔'), name_str.index('〕')
    else:
        return name_str
    name_str = name_str[:idx_a] + name_str[idx_b + 1:]
    return check_name(name_str)


def reverse_str_by_limit(my_str):
    tags = ['a', 'an', 'the']
    str_list = my_str.split(' ')
    new_list = []

    is_pass = False
    for idx, v in enumerate(str_list):
        if idx + 1 == len(str_list):
            new_list.append(v)
            break
        if is_pass:
            is_pass = False
            continue
        if v not in tags:
            new_list.append(v)
        else:
            if str_list[idx + 1] not in tags:
                new_list.append(v + ' ' + str_list[idx + 1])
                is_pass = True
            else:
                new_list.append(v)
    new_list.reverse()
    return ' '.join(new_list)


def list_subsets_0(numbers, k):
    return list(map(set, itertools.combinations(numbers, k)))


def list_subsets_1(numbers, k):
    result = [[]]
    for num in numbers:
        for _num in result[:]:
            tag = _num[:]
            tag.append(num)
            result.append(tag)
    ret = [set(_) for _ in result if len(_) == k]
    return ret


if __name__ == '__main__':
    # test_name_str = '[美][加]伽利略'
    # test_name_str = 'hh'
    # print(check_name(test_name_str))

    test_str = 'this is a pen on the desk but a an'
    print(reverse_str_by_limit(test_str))

    # test_numbers = {1, 2, 3, 4}
    # test_k = 3
    # print(list_subsets_0(test_numbers, test_k))
    # print(list_subsets_1(test_numbers, test_k))
