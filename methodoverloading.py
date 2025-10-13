class Add:
    def sum(self, a=None, b=None, c=None):
        if a and b and c is not None:
            print("Sum of three numbers:", a + b + c)
        elif a and b is not None:
            print("Sum of two numbers:", a + b)
        else:
            print("Please provide at least two numbers")

obj = Add()

obj.sum(5, 10)    
obj.sum(5, 10, 15)   
obj.sum(5)          
