"""
乐信圣文 20220222
读取json文件根据分数进行排名
"""
import json


def get_ranking():
    with open('score.json', encoding='utf8') as f:
        my_dict = json.load(f)

    new_ranking = {}
    for kk, vv in my_dict.items():
        child = sorted(vv.items(), key=lambda vv: vv[1])
        new = []
        for idx, v in enumerate(child):
            if idx == 0:
                new.append([v[0], 1])
            else:
                if v[1] == child[idx - 1][1]:
                    new.append([v[0], new[idx - 1][1]])
                else:
                    new.append([v[0], idx + 1])
        new_ranking[kk] = {_[0]: _[1] for _ in new}
    print(new_ranking)


if __name__ == '__main__':
    get_ranking()
