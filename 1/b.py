l1= []
l2 = []
with open("input", "r") as inp:
    for nums in inp:
        n1, n2 = nums.split("   ")
        l1.append(int(n1))
        l2.append(int(n2))

l1.sort()
l2.sort()
sim_score = 0
for n1 in l1:
    sim_score += n1 * [n1 == n2 for n2 in l2].count(True)

print(sim_score)
