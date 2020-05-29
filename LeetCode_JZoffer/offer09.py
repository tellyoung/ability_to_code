class CQueue:

    def __init__(self):
        self.inpt = []
        self.oput = []

    def appendTail(self, value: int) -> None:
        self.inpt.append(value)
        
    def deleteHead(self) -> int:
        if len(self.oput) != 0:
            return self.oput.pop(-1)
        elif len(self.inpt) == 0:
            return -1
        else:
            while self.inpt:
                self.oput.append(self.inpt.pop(-1))
            return self.oput.pop(-1)

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()