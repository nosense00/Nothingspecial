# run_bf.py -- simple Brainfuck interpreter
import sys
def run_bf(code, inp=""):
    tape = [0]*30000
    ptr = 0
    pc = 0
    input_ptr = 0
    out = []
    stack = []
    bracket_map = {}
    for i,c in enumerate(code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            j = stack.pop()
            bracket_map[i] = j
            bracket_map[j] = i
    while pc < len(code):
        c = code[pc]
        if c == '>': ptr += 1
        elif c == '<': ptr -= 1
        elif c == '+': tape[ptr] = (tape[ptr] + 1) % 256
        elif c == '-': tape[ptr] = (tape[ptr] - 1) % 256
        elif c == '.': out.append(chr(tape[ptr]))
        elif c == ',': 
            if input_ptr < len(inp):
                tape[ptr] = ord(inp[input_ptr]); input_ptr += 1
            else:
                tape[ptr] = 0
        elif c == '[' and tape[ptr] == 0:
            pc = bracket_map[pc]
        elif c == ']' and tape[ptr] != 0:
            pc = bracket_map[pc]
        pc += 1
    return ''.join(out)

if __name__ == '__main__':
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        code = ''.join(ch for ch in f.read() if ch in "<>+-.,[]")
    print(run_bf(code))
