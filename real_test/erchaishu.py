def test(my_input):
    aa = []
    bb = []

    for s in my_input:
        s_split = s.split(',')
        aa.append(int(s_split[0].split("(")[1]))
        bb.append(int(s_split[1].split(")")[0]))

    aa = [1, 2, 5, 7, 9]
    bb = [2, 4, 7, 2, 5]

    child_list = []  # len = 2
    center_list = []  # len = 1
    prent_list = []  # len = 1

    for a in aa:
        if bb.count(a) == 2:
            center_list.append(a)
        if a not in bb:
            child_list.append(a)

    if len(child_list) != 2:
        return False
    if len(center_list) != 1:
        return False

    for b in bb:
        if b not in aa:
            prent_list.append(b)

    if len(prent_list) != 1:
        return False

    return True


if __name__ == '__main__':
    aaa = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
    ret = test(aaa)
    print(ret)
