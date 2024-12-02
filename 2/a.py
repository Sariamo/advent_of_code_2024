l = []
with open("input", "r") as inp:
    for nums in inp:
        l.append([int(num) for num in nums.split(" ")])

safe_count = 0
for ln in l:
    all_incr = True
    all_decr = True
    differences_small_enough = True
    for i in range(len(ln) - 1):
        if ln[i] == ln[i + 1] or abs(ln[i] - ln[i + 1]) > 3:
            differences_small_enough = False
            break
        if ln[i] < ln[i + 1] <= ln[i] + 3:
            all_decr = False
        if ln[i + 1] < ln[i] <= ln[i + 1] + 3:
            all_incr = False
    if (all_decr or all_incr) and differences_small_enough:
        safe_count += 1

print(safe_count)
