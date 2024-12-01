l1= []
l2 = []
with open("input", "r") as inp:
    for nums in inp:
        n1, n2 = nums.split("   ")
        l1.append(int(n1))
        l2.append(int(n2))

l1.sort()
l2.sort()
dist = 0
for i in range(len(l1)):
    dist += abs(l1[i] - l2[i])

print(dist)
