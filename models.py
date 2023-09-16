"""
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке.
"""


class Stack:

    def __init__(self, stack: str):
        self.stack = stack
        self.open_parentheses = "([{"
        self.close_parentheses = ")]}"
        self.check_list = ""

    def is_empty(self) -> bool:
        return len(self.stack) > 0

    def push(self, element: str):
        self.stack += element

    def pop(self):
        res = self.stack[-1]
        self.stack = self.stack[0:-1]
        return res

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def correct_incorrect(self):

        if self.size() > 0:
            element = self.stack[-1]
            if element in self.close_parentheses:
                self.check_list += self.pop()
                self.correct_incorrect()
            elif element in self.open_parentheses and self.close_parentheses.index(
                    self.check_list[-1]) == self.open_parentheses.index(element):
                self.check_list = self.check_list[0:-1]
                self.pop()
                self.correct_incorrect()
        if self.size() == 0 and len(self.check_list) == 0:
            return "Correct"
        else:
            return "Incorrect"
