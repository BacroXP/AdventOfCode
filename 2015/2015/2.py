import libs.input

packets = libs.input.file()
packets = libs.input.nums(packets, True)

# Part 1
print(sum([2 * (l * w + w * h + h * l) + min(l * w, w * h, h * l) for l, w, h in packets]))

# Part 2
print(sum([l * w * h + 2 * (l + w) for l, w, h in packets]))
