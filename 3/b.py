import numbers

s = ""
with open("input", "r") as file:
    for line in file:
        s += str(line)

res = 0
do = True
for i in range(s.count("mul(") + 1):
    try:
        if i > 1:
            off = s.split("mul(")[i - 1].split("mul(")[-1]

            if "don't()" in off and ("do()" not in off or ("do()" in off and off.rfind("don't()") > off.rfind("do()"))):
                do = False
                continue
            else:
                if "do()" in off:
                    do = True

        if do:
            subs = s.split("mul(")[i].split(")")[0]
            a = int(subs.split(",")[0])
            b = int(subs.split(",")[1])
            if len(subs.split(",")) == 2 and isinstance(int(a), numbers.Number) and isinstance(int(b), numbers.Number) \
                    and isinstance(float(subs.replace(",", ".")), numbers.Real) and " " not in subs:
                res += int(a)*int(b)
    except:
        continue

print(res)
