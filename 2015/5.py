import libs.input

words = libs.input.grid()
sol = 0

for word in words:
    if word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u") >= 3:
        fine = True
        doubles = False

        for pair in libs.input.pairs(word):
            if pair[0] == pair[1]:
                doubles = True

            if pair in [("a", "b"), ("c", "d"), ("p", "q"), ("x", "y")]:
                fine = False
            
        sol += 1 if fine and doubles else 0

# Part 1
print(sol)

sol = set()

for i, word in enumerate(words):
    doubles = False
    pairs = set()
    pairs_list = {}

    for j, pair in enumerate(libs.input.pairs(word)):
        if pair in pairs:
            if j - pairs_list[pair] != 1:
                doubles = True
                break
            else:
                continue
        
        pairs.add(pair)
        pairs_list[pair] = j

    fine = False
    for triple in libs.input.triples(word):
        if triple[0] == triple[2]:
            fine = True

    if fine and doubles:
        sol.add(i)

# Part 2
print(len(sol))
