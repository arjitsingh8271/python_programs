class Calculator:
    def set(self,a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

  
    
num1 = int(input())     
num2 = int(input())     

c = Calculator()
c.set(num1,num2)

print(c.sum())
print(c.subtraction())
print(c.multiplication())
print(c.division())