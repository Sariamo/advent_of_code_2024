l = ""
with open("input", "r") as inp:
    for line in inp:
        l += str(line)

occupied = True
isl = []
id = 0
for storage in l:
    if occupied:
        for _ in range(int(storage)):
            isl.append(str(id))
        id += 1
        occupied = False
    else:
        for _ in range(int(storage)):
            isl.append(".")
        occupied = True

right_ptr = len(isl) - 1
while 0 <= right_ptr:
    while isl[right_ptr] == ".":
        right_ptr -= 1
    id = isl[right_ptr]
    l = 0
    while isl[right_ptr - l] == id:
        l += 1
    for left_ptr in range(right_ptr):
        while isl[left_ptr] != ".":
            left_ptr += 1
        g = 0
        while left_ptr + g < right_ptr and isl[left_ptr + g] == "." and g < l:
            g += 1
        if l <= g:
            for le in range(l):
                isl[left_ptr + le] = isl[right_ptr - le]
                isl[right_ptr - le] = "."
            break

    print(right_ptr)
    right_ptr -= l

sum = 0
for i, id in enumerate(isl):
    if id != ".":
        sum += i*int(id)
print(sum)