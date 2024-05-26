class abc:
    def __init__(self, n, r):
        self.n = "aaa"
        self.r = 9

    def dis(self):
        print(self.n, self.r)

s = abc()
s.dis()
print(s.__dict__)