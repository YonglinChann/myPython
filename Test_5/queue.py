class queue:
    def __init__(self, size = 5):
        self.content = []
        self.size = size
        self.current = 0
    def setSize(self, size):
        if size < self.current:
            for i in range(size, self.current)[::-1]:
                del self.content[i]
            self.current = size
        self.size = size
    def put(self, v):
        if self.current < self.size:
            self.content.append(v)
            self.current = self.current + 1
        else:
            print('队列已满，正在等待…')
    def get(self,timeout = 60):
        if self.content:
            self.current = self.current - 1
            return self.content.pop(0)
        else:
            print('队列是空的')
    def show(self):
        if self.content:
            print(self.content)
        else:
            print('队列是空的')
    def empty(self):
        self.content = []
        self.current = 0
    def isempty(self):
        if not self.content:
            return True
        else:
            return False
    def isfull(self):
        return self.current == self.size

if __name__ == '__main__':
    print('使用模块')