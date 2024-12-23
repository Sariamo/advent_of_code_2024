def is_ordered(s):
    already_at_points = False
    for st in s:
        if st == ".":
            already_at_points = True
        elif already_at_points:
            return False
    return True


l = ""
with open("input", "r") as inp:
    for line in inp:
        l += str(line)

occupied = True
id_str_list = []
id = 0
for storage in l:
    if occupied:
        for _ in range(int(storage)):
            id_str_list.append(str(id))
        id += 1
        occupied = False
    else:
        for _ in range(int(storage)):
            id_str_list.append(".")
        occupied = True

left_ptr = 0
right_ptr = len(id_str_list) - 1
while not is_ordered(id_str_list):
    if id_str_list[left_ptr] == "." and id_str_list[right_ptr] != ".":
        id_str_list[left_ptr] = id_str_list[right_ptr]
        id_str_list[right_ptr] = "."
    if left_ptr == right_ptr:
        break
    while id_str_list[left_ptr] != ".":
        left_ptr += 1
    while id_str_list[right_ptr] == ".":
        right_ptr -= 1

sum = 0
for i, id in enumerate(id_str_list):
    if id != ".":
        sum += i*int(id)
print(sum)
