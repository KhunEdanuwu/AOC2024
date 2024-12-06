with open("input/Day5.txt") as f:
    lines = f.readlines()

rules_to_map = []
updates = []

# Get rules to map and upadtes in seprate var
for i in lines:
    if '|' in i:
        formated = [int(x) for x in i.strip().split('|')]
        rules_to_map.append(formated)
    elif i.strip() == '':
        continue
    else:
        formated = [int(x) for x in i.split(',')]
        updates.append(formated)

# print(rules_to_map)
# print("----------------------")
print(updates)
# tt = [[int(x) for x in i.split('|')] for i in lines]
# init mapping (key = int, value = list of value that must come before key)
map = {}
for i in rules_to_map:
    if i[1] not in map:
        map[i[1]] = []
    map[i[1]].append(i[0])

# print(lines[0])
# print("---------")
# print(tt)
print("---------")
print(map)

def dfs():
    pass

      
        
def is_update_order_correct(update: list[int]):
    # Check pour chaque elem si les autres elems sont mappé en tant que "doit venir avant" 
    # Si présent et index > à elem en cours alors False si aucun ne amtch cette condition ils sont bien rangés
    for index, elem in enumerate(update):
        if elem in map.keys():
            for x in map[elem]:
                if x in update:
                    if update.index(x) > index:
                        return False
    return True

#     return True

tt = 0
for i in updates:
    res = is_update_order_correct(i)
    if res:
        middle_index = int((len(i))/2)
        middle_num = i[middle_index]
        tt += middle_num
        
    print(f"[{i}] -- {res}")
    
print(tt)