class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1.pop(-1))
        res = self.stack2.pop(-1)
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop(-1))
        return res
if __name__ == "__main__":
    a = ["PSH1", "PSH2", "PSH3", "POP", "POP", "PSH4", "POP", "PSH5", "POP", "POP"]

    push(1)
    push(2)
    push(3)
    print(pop())
    print(pop())
    push(4)
    print(pop())
    push(5)
    print(pop())
    print(pop())