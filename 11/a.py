nums = []
with open("input", "r") as inp:
    for numbers in inp:
        numbers_list = numbers.split(" ")
        for number in numbers_list:
            nums.append(int(number))

blink_times = 25
for bt in range(blink_times):
    new_list = []
    for num in nums:
        if num == 0:
            new_list.append(1)
        elif len(str(num)) % 2 == 0:
            len_num_half = int(len(str(num)) / 2)
            first_half = int(str(num)[:len_num_half])
            new_list.append(first_half)
            second_half = str(num)[len_num_half:]
            if second_half != "":
                second_half = int(second_half)
                new_list.append(second_half)
        else:
            new_list.append(num*2024)
    nums = new_list
    print(bt)

print(len(nums))
