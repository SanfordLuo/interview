"""
乐信圣文 20220222
读取json文件根据分数进行排名
"""
import json


def run():
    with open('./score.json') as f:
        data = json.load(f)

    new_dict = {}

    for item in data.items():
        new_child = sorted(item[1].items(), key=lambda x: x[1], reverse=True)
        # print(new_child)

        new_new_child = {}
        for idx, v_child in enumerate(new_child):
            if idx == 0:
                new_new_child[v_child[0]] = 1
            else:
                if v_child[1] == new_child[idx - 1][1]:
                    old_name = new_child[idx - 1][0]
                    new_new_child[v_child[0]] = new_new_child[old_name]
                else:
                    new_new_child[v_child[0]] = idx + 1

        new_dict[item[0]] = new_new_child

    print(new_dict)


if __name__ == '__main__':
    run()
