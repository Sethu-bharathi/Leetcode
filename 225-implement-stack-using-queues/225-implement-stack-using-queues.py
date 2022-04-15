class MyStack:

    def __init__(self):
        self.queue1=[]
        self.queue2=[]

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))
        while len(self.queue2)>1:
            self.queue1.append(self.queue2.pop(0))
        temp=self.queue2[0]
        self.queue2=[]
        return temp
    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return len(self.queue1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()