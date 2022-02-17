"""
豆瓣 20220216
1、在显示外国作者姓名时，豆瓣会按照惯例展示国籍，如 [奥] 卡夫卡，[日] 村上春树 等。用户添加作者数据时使用括号可能不规范或不匹配，如【德】，惠特曼[美]，[英]等；也可能有多国籍的作者，如 [美][加]。假设括号类型只有四种：()，[]，【】,〔〕，请使用你熟悉的编程语言将国籍信息从作者姓名字符串中去除，考虑前述及其他可能的特殊情况。
3、假设字符串仅由英文单词组成，写一个程序颠倒其中单词的顺序，如“fine by me”处理后变为“me by fine”。但量词（a/an/the）后面如果跟随了一个非量词，那么这两个词应看做一个完整的单词，如“this is a pen on the desk but a an”，处理后应为：“an a but the desk on a pen is this”。请附上你的程序时间复杂度及测试用例
5、You are given a set of numbers 0-n.Given a k,print all subsets of size k.
"""


def func_five(numbers, k):
    result = [[]]
    for num in numbers:
        for numm in result[:]:
            ret = numm[:]
            ret.append(num)
            result.append(ret)
            if len(ret) == k:
                print(ret)


if __name__ == '__main__':
    func_five(numbers={1, 2, 3, 4, 5}, k=3)
