import re

# PART1

 

# with open("input/Day3.txt") as f:

#     lines = f.readlines()

 

# occurences = []

# for i in lines:

#     occurences.append(re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\))", i))

 

# tt = 0

# for i in occurences:

#     for x in i:

#         num = x[4:-1].split(",")

#         print(f"{int(num[0])}x{int(num[1])}")

#         tt += int(num[0]) * int(num[1])

# print(tt)

with open("input/Day3.txt") as f:
    lines = f.read()
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, lines)

res = 0
enable = True
for match in matches:
    if match == "do()":
        enable = True
    elif match == "don't()":
        enable = False
    else:
        if enable:
            x, y = map(int, match[4:-1].split(","))
            res += x * y

print(res)

 