import libs.input

def compute_memory_size(string):
    string = string[1:-1]

    memory_size = 0
    i = 0
    while i < len(string):
        if string[i] == "\\":
            if string[i + 1] in ['\\', '"']:
                memory_size += 1
                i += 2
            elif string[i + 1] == 'x':
                memory_size += 1
                i += 4
        else:
            memory_size += 1
            i += 1

    return memory_size

def compute_encoded_size(string):
    encoded_size = 2  # Account for the new surrounding quotes
    for char in string:
        if char in ['\\', '"']:
            encoded_size += 2  # Escaped backslash or quote
        else:
            encoded_size += 1  # Regular character
    return encoded_size

lines = libs.input.file()
code_size = sum([len(line) for line in lines])
memory_size = 0
encoded_size = 0

for line in lines:
    memory_size += compute_memory_size(line)
    encoded_size += compute_encoded_size(line)

# Part 1
print(code_size - memory_size)

# Part 2
print(encoded_size - code_size)
