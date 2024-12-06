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
# print(updates)
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
# print("---------")
print(map)
      
# PArt 1    
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

tt = 0
for i in updates:
    res = is_update_order_correct(i)
    if res:
        middle_index = int((len(i))/2)
        middle_num = i[middle_index]
        tt += middle_num
        
    print(f"[{i}] -- {res}")
    
print(tt)

#Part 2
# Si jamais je reviens dessus:
# On passe sur les elem de l'update pour chaque on check si il y a une règle et 
# si une n'est pas appliqué 
# => On enregistre la pos de l'elem et de l'elem qui respecte pas la règle

# En suite on les swap
#Marche avec l'input de base
new_upadtes = []
for i in updates:
    res = is_update_order_correct(i)
    if not res:
        incorect_ordered_update = []
        for index, elem in enumerate(i):
            if elem in map.keys():
                for x in map[elem]:
                    if x in i:
                        if i.index(x) > index:
                            incorect_ordered_update.append((i.index(x), index))
        
        for x in incorect_ordered_update:
            i[x[0]], i[x[1]] = i[x[1]], i[x[0]]
        new_upadtes.append(i)

print("-----")
print(new_upadtes)
tt = 0
for i in new_upadtes:
    middle_index = int((len(i))/2)
    middle_num = i[middle_index]
    tt += middle_num
    
print(tt)

# 97,75,47,61,53 || 61,29,13 || 97,75,47,29,13

# The fourth update, 75,97,47,61,53, is not in the correct order: 
# it would print 75 before 97, which violates the rule 97|75.

# 61,13,29 =>  29|13.   
# => 1: 29, 61, 13
# => 2: 61, 29, 13

# for i in updates:
#     res = is_update_order_correct(i)
#     if not res:
#         reorder_update = reorder_update(i)

# Marche po good answer 4507 ! No double star