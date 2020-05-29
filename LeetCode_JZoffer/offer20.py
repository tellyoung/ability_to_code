class Solution:
    def __init__(self):
        self.p = 0

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0:
            return False
        number = self.scanint(s)
        if self.p == len(s):
            return number

        if self.p <= len(s) - 1 and s[self.p] == '.':
            self.p += 1
            if self.p == len(s):
                return number
            number = self.scanunsignint(s) or number

        if self.p <= len(s) - 1 and s[self.p] in ['e', 'E']:
            self.p += 1
            if self.p == len(s):
                return False
            number =  number and self.scanint(s)

        if self.p < len(s):
            return False

        return number

    def scanint(self, s):
        if s[self.p] in ['+', '-']:
            self.p += 1
        return self.scanunsignint(s)

    def scanunsignint(self, s):
        pre = self.p 
        while self.p < len(s) and s[self.p].isdigit():
            self.p += 1
        return self.p > pre