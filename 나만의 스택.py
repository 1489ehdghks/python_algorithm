class myStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def display(self):
        print(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        if self.stack[-1] == None:
            return print("아직 덜 찼습니다.")
        else:
            return print("가득 찼습니다.")

    def push(self, item):
        if self.isFull():
            print("가득 찼습니다.")
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f"{item}이 추가되었습니다.")

    def pop(self):
        if self.isEmpty():
            print("스택이 비어 있습니다.")
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"{item}이 제거되었습니다.")
            return item


Stack = myStack(5)
Stack.display()
print(Stack.isEmpty())
Stack.push(1)
Stack.push(2)
Stack.push(3)
Stack.push(4)
Stack.display()
Stack.pop()
Stack.display()
Stack.isFull()
Stack.push(4)
Stack.push(5)
Stack.display()
Stack.isFull()
