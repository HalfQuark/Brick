from sys import exit
print("Script:")
path = input()
f = open(path, "r")
print("-----")
file = []
goto_map = [-1]
i = 0
for l in f:
    if l.endswith("\n"):
        l = l[:-1]
    goto_map += [i]
    if l == "":
        continue
    sl = l.split("\\")
    i += len(sl)
    file += sl
goto_map += [i + 1]
stack = []
mem = []
line_i = 0

def stack_push(value):
    global stack
    stack = [value] + stack

def stack_pop(remove=True):
    global stack
    if not stack:
        raise_exception(f"Tried to pop empty stack")
    r = stack[0]
    if remove:
        stack = stack[1:]
    return r

def memory_get(idx):
    global mem
    if type(idx) != int:
        raise_exception(f"Memory get index {idx} not an integer")
    if idx < 0 or idx >= len(mem):
        raise_exception(f"Memory get index {idx} out of bounds")
    return mem[idx]

def memory_set(idx, value):
    global mem
    if type(idx) != int:
        raise_exception(f"Memory set index {idx} not an integer")
    if idx < 0:
        raise_exception(f"Memory set index {idx} out of bounds")
    if idx >= len(mem):
        mem += [None]*(idx - len(mem) + 1)
    mem[idx] = value

def parse_value(x):
    value = None
    try:
        value = int(x)
    except:
        try:
            value = float(x)
        except:
            value = x
    return value

def raise_exception(e):
    print(f"Exception raised at line {i_to_line(line_i)}: {e}")
    exit(0)

def i_to_line(idx):
    i = 0
    while i < len(goto_map) and goto_map[i] <= idx:
        i += 1
    return i - 1

while line_i < len(file):
    line = file[line_i]
    if line.endswith("\n"):
        line = line[:-1]
    if line == "SET":
        idx = stack_pop()
        value = stack_pop()
        memory_set(idx, value)
    elif line == "GET":
        idx = stack_pop()
        value = memory_get(idx)
        stack_push(value)
    elif line == "POP":
        stack_pop()
    elif line == "IN":
        value = input()
        stack_push(parse_value(value))
    elif line == "OUT":
        value = stack_pop()
        print(value)
    elif line == "GOTO":
        idx = stack_pop()
        if type(idx) != int:
            raise_exception(f"GOTO index {idx} not an integer")
        if idx < 0 or idx >= len(goto_map):
            raise_exception(f"GOTO index {idx} out of bounds")
        line_i = goto_map[idx] - 1
    elif line == "END":
        break
    elif line == "+":
        b = stack_pop()
        a = stack_pop()
        try:
            value = a + b
        except:
            raise_exception(f"Tried to apply {line} to {a} and {b}")
        else:
            stack_push(value)
    elif line == "-":
        b = stack_pop()
        a = stack_pop()
        try:
            value = a - b
        except:
            raise_exception(f"Tried to apply {line} to {a} and {b}")
        else:
            stack_push(value)
    elif line == "*":
        b = stack_pop()
        a = stack_pop()
        try:
            value = a * b
        except:
            raise_exception(f"Tried to apply {line} to {a} and {b}")
        else:
            stack_push(value)
    elif line == "/":
        b = stack_pop()
        a = stack_pop()
        try:
            value = a / b
        except:
            raise_exception(f"Tried to apply {line} to {a} and {b}")
        else:
            stack_push(value)
    elif line == "=":
        b = stack_pop()
        a = stack_pop()
        if a != b:
            line_i = goto_map[i_to_line(line_i) + 1] - 1
    elif line == "<":
        b = stack_pop()
        a = stack_pop()
        try:
            if not a < b:
                line_i = goto_map[i_to_line(line_i) + 1] - 1
        except:
            raise_exception(f"Tried to compare {a} and {b}")
    elif line == ">":
        b = stack_pop()
        a = stack_pop()
        try:
            if not a > b:
                line_i = goto_map[i_to_line(line_i) + 1] - 1
        except:
            raise_exception(f"Tried to compare {a} and {b}")
    elif line == "DEBUG":
        print(stack)
        print(mem)
    else:
        stack_push(parse_value(line))
    line_i += 1

