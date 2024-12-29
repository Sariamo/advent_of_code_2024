import os

file = ["help_file1", "help_file2"]
[os.remove(f) for f in file if os.path.isfile(f)]

with open("input", "r") as inp:
    with open(file[0], "w") as f:
        for row in inp:
            f.write(row)
        f.write(".")

file_index = 0
for i in range(75):
    print()
    print(i)
    index = 0
    first = True
    end = False
    while True:
        with open(file[file_index], "r") as inp:
            inp.seek(index)
            num = ""
            while True:
                token = inp.read(1)
                if token != "\n" and token != " " and token != "" and token != ".":
                    num += token
                    index += 1
                elif token == ".":
                    end = True
                    break
                elif num != "":
                    index += 1
                    print(num)
                    num = int(num)
                    file_name = file[(file_index + 1) % 2]
                    if os.path.isfile(file_name) and first:
                        os.remove(file_name)
                        first = False
                    with open(file_name, "a") as out:
                        if num == 0:
                            out.write(str(1))
                        elif len(str(num)) % 2 == 0:
                            len_num_half = int(len(str(num)) / 2)
                            first_half = int(str(num)[:len_num_half])
                            out.write(str(first_half))
                            second_half = str(num)[len_num_half:]
                            if second_half != "":
                                second_half = int(second_half)
                                out.write(" ")
                                out.write(str(second_half))
                        elif len(str(num)) % 2 == 1:
                            out.write(str(num*2024))
                        out.write(" ")
                    break
            if end:
                break
    file_index = (file_index + 1) % 2
