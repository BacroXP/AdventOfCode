import libs.input

file = libs.input.grid()[0]

# Part 1
print(file.count("(") - file.count(")"))

file.reverse()
i = 1
temp = [file.pop()]

while temp.count("(") - temp.count(")") != -1:
    i += 1
    temp.append(file.pop())

# Part 2
print(i)
