l = []
with open("input", "r") as inp:
    for nums in inp:
        ln = [int(num) for num in nums.split(" ")]
        lns_with_one_missing = [[ln[i] for i in range(len(ln)) if i != j] for j in range(len(ln))]
        l.append(lns_with_one_missing)

safe_count = 0
for ln in l:
    found_one = False
    for ln_variant in ln:
        if found_one:
            break
        all_incr = True
        all_decr = True
        differences_small_enough = True
        for i in range(len(ln_variant) - 1):
            if ln_variant[i] == ln_variant[i + 1] or abs(ln_variant[i] - ln_variant[i + 1]) > 3:
                differences_small_enough = False
                break
            if ln_variant[i] < ln_variant[i + 1] <= ln_variant[i] + 3:
                all_decr = False
            if ln_variant[i + 1] < ln_variant[i] <= ln_variant[i + 1] + 3:
                all_incr = False
        if (all_decr or all_incr) and differences_small_enough:
            safe_count += 1
            found_one = True

print(safe_count)
