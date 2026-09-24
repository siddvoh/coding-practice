import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length: int, width: int = None) -> None:
        return length*width if width else round(length*length*math.pi, 2)
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
