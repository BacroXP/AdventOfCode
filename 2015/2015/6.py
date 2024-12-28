import libs.input

cmds = libs.input.file()
nums = libs.input.nums(cmds)
cmds = [False if cmd.split(" ")[1] == "off" else True if cmd.startswith("turn") else "toggle" for cmd in cmds]

lights = [[False] * 1001 for i in range(1001)]

for i, cmd in enumerate(cmds):
    for j in range(nums[i][0] - 1, nums[i][2]):
        for k in range(nums[i][1] - 1, nums[i][3]):
            if cmd != "toggle":
                lights[j][k] = cmd
            else:
                lights[j][k] = not lights[j][k]

# Part 1
print(sum([row.count(True) for row in lights]))

cmds = libs.input.file()
nums = libs.input.nums(cmds)
cmds = [-1 if cmd.split(" ")[1] == "off" else 1 if cmd.startswith("turn") else 2 for cmd in cmds]

lights = [[0] * 1001 for i in range(1001)]

for i, cmd in enumerate(cmds):
    for j in range(nums[i][0] - 1, nums[i][2]):
        for k in range(nums[i][1] - 1, nums[i][3]):
            lights[j][k] += cmd
            if lights[j][k] < 0:
                lights[j][k] = 0

# Part 2
print(sum([sum(row) for row in lights]))
