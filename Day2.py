# # PArt 1
# with open("Day2.txt") as f:
#     lines = [i.split() for i in f.readlines()]

# tt_valid = 0
# for z, x in enumerate(lines):
#     #Set orderdering
#     if int(x[0]) < int(x[1]):
#         is_asc = True 
#     elif int(x[0]) > int(x[1]):
#         is_asc = False 
#     elif abs(int(x[0]) - int(x[1])) == 0:
#         tt_valid += 1
#         continue
    
#     if abs(int(x[0]) - int(x[1])) > 3:
#         tt_valid += 1
#         continue
#     else:
#         is_safe = True
        
#     curr_num = int(x[0])
#     for y in range(1,len(x)):
#         if abs(int(x[y]) - curr_num) > 3:
#             tt_valid += 1
#             break
        
#         if is_asc:
#             if int(x[y]) > curr_num:
#                 pass
#             else:
#                 tt_valid += 1
#                 break
        
        
#         if not is_asc:
#             if int(x[y]) < curr_num:
#                 pass
#             else:
#                 tt_valid += 1
#                 break
            
#         curr_num = int(x[y])
# print(len(lines) - tt_valid)
# print(tt_valid)


# APrt 2

def is_safe(report:list[int]) -> bool:
    elem_invalid = 0
    for y, x in enumerate(report):
        if y == 0:
            if x == report[y+1]:
                elem_invalid += 1
                break
            elif x > report[y+1]:
                ordering = 'desc'
            elif x < report[y+1]:
                ordering = 'asc'
            
            if abs(x - report[y+1]) > 3:
                elem_invalid += 1
                
            
            
        else:
            if abs(curr_num - x) > 3 or abs(curr_num - x) == 0:
                elem_invalid += 1
            
            if ordering == "asc":
                if curr_num > x:
                    elem_invalid += 1
            elif ordering == "desc":
                if curr_num < x:
                    elem_invalid += 1
        curr_num = x
                        
    if elem_invalid > 0:
        #print(f"NOT VALID: report {report}, nb error {elem_invalid}")
        return False
    else:
        #print(f"VALID: report {report} , nb error {elem_invalid}")
        return True

with open("Day2.txt") as f:
    lines = [[int(num) for num in i.split()] for i in f.readlines()]
#print(lines)
tt = 0
list_unsafe = []
for x in lines:
    #print(x)
    if not is_safe(x):
        list_unsafe.append(x)

print(len(lines) - len(list_unsafe))
yy = 0
for z in list_unsafe:
    new_safe = 0
    for y,x in enumerate(z):
        list_to_test = z[:y] + z[y+1:]
        res = is_safe(list_to_test)
        if res:
            new_safe +=1
    if new_safe > 0:
        yy +=1 
print(yy)
print(len(lines) - len(list_unsafe) + yy)
        



# tt_invalid = 0
# for z, x in enumerate(lines):
#     elem_invalid = 0
#     #Set orderdering
#     if int(x[0]) < int(x[1]):
#         is_asc = True 
#     elif int(x[0]) > int(x[1]):
#         is_asc = False 
#     elif abs(int(x[0]) - int(x[1])) == 0:
#         elem_invalid += 1
#         continue
    
#     if abs(int(x[0]) - int(x[1])) > 3:
#         elem_invalid += 1
#         continue
#     else:
#         is_safe = True
        
#     curr_num = int(x[0])
#     for y in range(1,len(x)):
#         if abs(int(x[y]) - curr_num) > 3:
#             elem_invalid += 1
#             continue
        
#         if is_asc:
#             if int(x[y]) > curr_num:
#                 pass
#             else:
#                 elem_invalid += 1
#                 continue
        
        
#         if not is_asc:
#             if int(x[y]) < curr_num:
#                 pass
#             else:
#                 elem_invalid += 1
#                 continue
            
#         curr_num = int(x[y])
#         if elem_invalid > 1:
#             tt_invalid += 1
#             break
        
# print(len(lines) - tt_invalid)
# print(tt_invalid)