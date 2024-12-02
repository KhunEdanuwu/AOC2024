#PART1 
with open(file="Day1_1.txt") as f:
    lines = [i.split() for i in f.readlines()]
    
left = []
right = []
for i in lines:
    left.append(int(i[0]))
    right.append(int(i[1]))

tt_dst = []
while len(left) > 0:
    dst = abs(min(left) - min(right))
    tt_dst.append(dst)
    left.remove(min(left))
    right.remove(min(right))
    
print(sum(tt_dst))


######################################################################################
#PART 2
with open(file="Day1_1.txt") as f:
    lines = [i.split() for i in f.readlines()]

left = []
right = []
for i in lines:
    left.append(int(i[0]))
    right.append(int(i[1]))

tt_sim = []
for i in left:
    i_cnt = 0
    for x in right:
        if x == i:
            i_cnt += 1
    tt_sim.append(i*i_cnt)
    
print(sum(tt_sim))
