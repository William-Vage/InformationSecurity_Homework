#!/bin/python3

# 期中大作业第四题 - 攻击者flag自动提取脚本
# 输入为0-5，分别对应着六个ip的index

import sys
import re

# 我们分到的6个ip后缀: 99.999.9.xx
ip_list = [11, 12, 17, 25, 26, 28]

# SQL正则匹配
# 不同同学可能使用不同的方法提取flag，所以这里的正则也是个数组，每一个regex对应一个ip
sql_regex = [
    "ascii\(substr\(\(select \* from flag\) from ([0-9]+) for 1\)\)", # no data
    "ascii\(substr\(\(select \* from flag\) from ([0-9]+) for 1\)\)", # succ
    "ascii\(substr\(\(select \* from flag\) from ([0-9]+) for 1\)\)", # no data
    "ascii\(substr\(\(select \* from flag\) from ([0-9]+) for 1\)\)", # register.php no username
    "ascii\(substr\(\(select \* from flag\) from ([0-9]+) for 1\)\)", # succ
    "ascii\(substr\(\(select \* from flag\) from ([0-9]+) for 1\)\)", # TODO: parse username
    ]

# 终止情形匹配
# 有些同学可能多次跑脚本提取flag，但并不是每一次跑脚本都跑全了
# 这里记录该同学最后一次完整提取flag的时间，以提前终止脚本，防止后面的不完全数据污染flag
end_regex = [
    None,
    None,
    None,
    None,
    "Apr 22, 2023 21:20:17.608746000",
    None
]

# flag提取正则
name_regex = '<span class=\\\\"user-name\\\\">\s+([0-9]+)\s+</span>'

flag = [0] * 50

idx = 0
ip = 0

# 输入检查
try:
    idx = int(sys.argv[1])
    ip = ip_list[idx]
except:
    print("error! index must be in [0,5]!")
    exit(1)

print(f"Processing idx {idx} ip {ip_list[idx]}!")

f = open(f"data/{ip_list[idx]}.json", "r")

prev_idx = -1
for str in f:
    if end_regex[idx] != None and re.search(end_regex[idx], str, re.IGNORECASE | re.DOTALL) != None:
        print("End of search reached, stopping.")
        break
    str = str.replace("\\n", "")
    sql_result = re.search(sql_regex[idx], str, re.IGNORECASE | re.DOTALL)
    name_result = re.search(name_regex, str, re.IGNORECASE | re.DOTALL)
    if (sql_result and len(sql_result.groups()) >= 1):
        # 正常情况下，每次攻击者SQL注入之后，都要访问index.php查看回显，所以这里直接将SQL注入时访问的flag位数记下来
        prev_idx = int(sql_result.group(1)) - 1
        print(f"prev index updated: {prev_idx}")
        continue
    if (name_result and len(name_result.groups()) >= 1):
        try:
            # 根据上一次SQL注入的flag位数，将flag那一位的内容记下来
            print(f"FLAG HIT: {int(name_result.group(1))}")
            if prev_idx >= 0:
                flag[prev_idx] = chr(int(name_result.group(1)))
                prev_idx = -1
        except:
            pass

# 输出结果
for i in flag:
    print(i, end="")

print()