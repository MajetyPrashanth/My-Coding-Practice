# class A(object):
#     def __init__(self,ID,name):
#         self.ID = ID
#         self.name = name
#     def display(self):
#         return self.ID, self.name
# a = A(1,"Ram")
# print(a.display())
class Stack:
    def __init__(self):
        self.stack = []
        pass
    def push(self,item):
        self.stack.append(item)
        pass
    def display(self):
        print(self.stack)
        pass
    def pop(self):
        print(self.stack.pop())
        pass
if __name__ == "__main__":
    stack = Stack()
    stack.display()
    stack.push(1)
    stack.push(10)
    stack.push(10)
    stack.push(10)
    stack.display()
    stack.pop()
    stack.display()
