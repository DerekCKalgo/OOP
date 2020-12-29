#multiple arguments   *nums can take in any number of arguments

class MathDojo:
    def __init__(self):
        self.result = 0
    	
    def add(self, num, *nums):
        self.result += num
        for a in nums:
            self.result+=a
        return self
    
    def subtract(self, num, *nums):
        self.result -= num
        for a in nums:
            self.result -= a
        return self



    
md = MathDojo()
a=md.add(2, 5, 6, 7).add(2).subtract(3,2, 2).result
print(a)
	

