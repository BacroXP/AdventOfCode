import libs.input
import libs.vars

cmds = libs.input.grid()[0]
pos = (0, 0)
s_pos = (0, 0)
r_pos = (0, 0)
temp = set((0, 0))
s_temp = set((0, 0))
dirs = libs.vars.dirs("<", "^", ">", "v")
santa = True

for cmd in cmds:
    if santa:
        s_pos = s_pos[0] + dirs[cmd][0], s_pos[1] + dirs[cmd][1]
        s_temp.add(s_pos)
    else:
        r_pos = r_pos[0] + dirs[cmd][0], r_pos[1] + dirs[cmd][1]
        s_temp.add(r_pos)
    
    pos = pos[0] + dirs[cmd][0], pos[1] + dirs[cmd][1]
    temp.add(pos)
    
    santa = not santa

s_temp.add((0, 0))

print(len(temp))
print(len(s_temp) - 1)
