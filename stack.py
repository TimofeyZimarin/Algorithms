import sys
class stack():

    def __init__(self, stack=[], maximum=[]):
        self.stack = stack
        self.maximum = maximum
    def push(self, elem):
        self.stack.append(elem)
        if len(self.maximum) > 0:
            if self.maximum[-1] > elem:
                self.maximum.append(self.maximum[-1])
            else:
                self.maximum.append(elem)
        else:
            self.maximum.append(elem)
    def pop(self):
        last = self.stack.pop()
        max_last = self.maximum.pop()
        return
    def max(self):
        return print(self.maximum[-1])

def main():
    reader = sys.stdin
    n = int(next(reader))
    commands = []
    for i in range(n):
        com = next(reader)
        commands.append(com.split())
    
    for i in range(len(commands)):
        if len(commands[i]) > 1:
            stack().push(int(commands[i][1]))
        elif commands[i][0] == 'pop':
            stack().pop()
        else:
            stack().max()

if __name__ == '__main__':
    main()
