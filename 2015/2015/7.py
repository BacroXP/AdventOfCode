import libs.input

cmds = libs.input.file()
nums = libs.input.nums(cmds)

vars = {}
corrupt_vars = {}
p1 = True

for i in range(1000):
    vars[str(i)] = i

while p1:
    todo, num = cmds.pop(0), nums.pop(0)
    
    cmd, sol = todo.split(" -> ")
    cmd = cmd.split(" ")
    
    if sol == "a":
        p1 = False
    
    if len(cmd) == 1 and num:
        vars[sol] = num[0]
        continue
    elif len(cmd) == 1:
        if cmd[0] in vars:
            vars[sol] = vars[cmd[0]]
            continue
    elif cmd[0] == "NOT":
        if cmd[1] in vars:
            vars[sol] = 65535 - vars[cmd[1]]
            continue
    elif cmd[1] == "AND":
        if cmd[0] in vars:
            if cmd[2] in vars:
                vars[sol] = vars[cmd[0]] & vars[cmd[2]]
                continue
    elif cmd[1] == "OR":
        if cmd[0] in vars:
            if cmd[2] in vars:
                vars[sol] = vars[cmd[0]] | vars[cmd[2]]
                continue
    elif cmd[1] == "RSHIFT":
        if cmd[0] in vars:
            vars[sol] = vars[cmd[0]] >> num[0]
            continue
    elif cmd[1] == "LSHIFT":
        if cmd[0] in vars:
            vars[sol] = vars[cmd[0]] << num[0]
            continue
    
    p1 = True

    cmds.append(todo)
    nums.append(num)

# Part 1
print(vars["a"])

cmds = libs.input.file()
nums = libs.input.nums(cmds)

vars = {}
p1 = True

for i in range(10000):
    vars[str(i)] = i

while p1:
    vars["b"] = 46065
    todo, num = cmds.pop(0), nums.pop(0)
    
    cmd, sol = todo.split(" -> ")
    cmd = cmd.split(" ")
    
    if sol == "a":
        p1 = False
    
    if len(cmd) == 1 and num:
        vars[sol] = num[0]
        continue
    elif len(cmd) == 1:
        if cmd[0] in vars:
            vars[sol] = vars[cmd[0]]
            continue
    elif cmd[0] == "NOT":
        if cmd[1] in vars:
            vars[sol] = 65535 - vars[cmd[1]]
            continue
    elif cmd[1] == "AND":
        if cmd[0] in vars:
            if cmd[2] in vars:
                vars[sol] = vars[cmd[0]] & vars[cmd[2]]
                continue
    elif cmd[1] == "OR":
        if cmd[0] in vars:
            if cmd[2] in vars:
                vars[sol] = vars[cmd[0]] | vars[cmd[2]]
                continue
    elif cmd[1] == "RSHIFT":
        if cmd[0] in vars:
            vars[sol] = vars[cmd[0]] >> num[0]
            continue
    elif cmd[1] == "LSHIFT":
        if cmd[0] in vars:
            vars[sol] = vars[cmd[0]] << num[0]
            continue
    
    p1 = True

    cmds.append(todo)
    nums.append(num)

# Part 2
print(vars["a"])
