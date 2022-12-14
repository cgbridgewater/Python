
### Create Class
class MathDojo:
    def __init__(self):
        self.result = 0

###  Add 
    def add(self, num, *nums):
        self.result += num
        for a in nums:
            self.result += a
        # print(self.result)
        return self


### Subtract
    def subtract(self, num, *nums):
        self.result -= num
        for a in nums:
            self.result -= a
        # print(self.result)
        return self

# create an instance:
md = MathDojo()
doMaths = MathDojo()


# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5

xyz = doMaths.add(22).add(2,15,21).subtract(32,28).result
print(xyz)  ### should print 0