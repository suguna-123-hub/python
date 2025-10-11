SEGMENTS = {
    '0': [" _ ", "| |", "|_|"],
    '1': ["   ", "  |", "  |"],
    '2': [" _ ", " _|", "|_ "],
    '3': [" _ ", " _|", " _|"],
    '4': ["   ", "|_|", "  |"],
    '5': [" _ ", "|_ ", " _|"],
    '6': [" _ ", "|_ ", "|_|"],
    '7': [" _ ", "  |", "  |"],
    '8': [" _ ", "|_|", "|_|"],
    '9': [" _ ", "|_|", " _|"],
    '+': ["   ", " _ ", " _ "],
    '-': ["   ", " _ ", "   "],
    '*': ["   ", "*", "   "],
    '%': [" _ ", "  |", "|_ "],
    '=': ["   ", " _ ", " _ "]
}

def parse_display(n, lines):
    chars = []
    for i in range(n):
        char = [lines[0][i*3:(i+1)*3], lines[1][i*3:(i+1)*3], lines[2][i*3:(i+1)*3]]
        chars.append(char)
    return chars

def match_segment(char):
    for k, v in SEGMENTS.items():
        if char == v:
            return k
    return None

def toggle_segment(char):
    toggled = []
    for i in range(3):
        for j in range(3):
            new_char = [list(row) for row in char]
            new_char[i][j] = ' ' if char[i][j] != ' ' else '_'
            new_char_str = [''.join(row) for row in new_char]
            symbol = match_segment(new_char_str)
            if symbol:
                toggled.append((symbol, new_char_str))
    return toggled

def evaluate(expr):
    total = int(expr[0])
    i = 1
    while i < len(expr) - 1:
        op = expr[i]
        num = int(expr[i+1])
        if op == '+':
            total += num
        elif op == '-':
            total -= num
        elif op == '*':
            total *= num
        elif op == '%':
            total %= num
        i += 2
    return total

def find_faulty(n, lines):
    chars = parse_display(n, lines)
    symbols = [match_segment(c) for c in chars]
    rhs = int(''.join(symbols[symbols.index('=')+1:]))
    for i in range(n):
        if symbols[i] == '=' or i > symbols.index('='):
            continue
        toggles = toggle_segment(chars[i])
        for new_sym, _ in toggles:
            new_expr = symbols[:]
            new_expr[i] = new_sym
            if evaluate(new_expr[:new_expr.index('=')]) == rhs:
                return i + 1
    return -1

# Input
n = int(input())
lines = [input() for _ in range(3)]
print(find_faulty(n, lines))
