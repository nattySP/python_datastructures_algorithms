# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def process(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_bracket = Bracket(next, i)
            opening_brackets_stack.append(opening_bracket)

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if not len(opening_brackets_stack):
                return i + 1
            temp = opening_brackets_stack.pop()
            if not temp.Match(next):
                return i + 1

    if len(opening_brackets_stack):
        pos = opening_brackets_stack[0].position + 1
        return pos
    else:
        return 'Success'

if __name__ == "__main__":
    text = sys.stdin.read()
    print(process(text))



    # Printing answer, write your code here
