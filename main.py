class Stack:
    def __init__(self, instance):
        self.instance = instance
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def check_brackets(self):
        if self.isEmpty():
            self.push(self.instance[0])
        for bracket in self.instance[1:]:
            if bracket == ')' and self.peek() == '(' \
                    or bracket == ']' and self.peek() == '['\
                    or bracket == '}' and self.peek() == '{':
                self.pop()
            else:
                self.push(bracket)
        if self.isEmpty():
            print('Сбалансированно')
        else:
            print('Несбалансированно')


# Сбалансированные и несбалансированные последовательности скобок для проверки программы:
brackets1 = '(((([{}]))))'
brackets2 = '[([])((([[[]]])))]{()}'
brackets3 = '{{[()]}}'
brackets4 = '}{}'
brackets5 = '{{[(])]}}'
brackets6 = '[[{())}]'

stack = Stack(brackets1)
stack.check_brackets()
