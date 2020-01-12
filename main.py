""""
Fractions Calculator (To be translated to C++) by Andrew Li
"""


class Fraction:
    """ a class for defining fractions """
    def __init__(self, top, bottom):
        """ top is numerator and bottom is denominator """
        self.top = top
        self.bottom = bottom

    def __str__(self):
        """ prints fraction """
        self.simplify()
        if self.bottom == 1:
            return f"{int(self.top)}"
        return f"{int(self.top)}/{int(self.bottom)}"

    def __add__(self, rhs):
        """ overloads + """
        if isinstance(rhs, int):
            rhs = Fraction(rhs, 1)
        elif isinstance(rhs, float):
            return self.to_float() + rhs

        lcm = int(self.lcm(self.bottom, rhs.bottom))
        self.lcm_apply(lcm, self, rhs)

        return Fraction(self.top + rhs.top, self.bottom)

    def __radd__(self, other):
        """ overloads + but backwards b/c of commutativity """
        return self.__add__(other)

    def __sub__(self, rhs):
        """ overloads - """
        if isinstance(rhs, int):
            rhs = Fraction(rhs, 1)
        elif isinstance(rhs, float):
            return self.to_float() - rhs
        lcm = self.lcm( self.bottom, rhs.bottom)
        self.lcm_apply(lcm, self, rhs)

        return Fraction(self.top - rhs.top, self.bottom)

    def __rsub__(self, lhs):
        """ overloads - but opposite """
        if isinstance(lhs, int):
            lhs = Fraction(lhs, 1)
        elif isinstance(lhs, float):
            return lhs - self.to_float()
        lcm = self.lcm( self.bottom, lhs.bottom)
        self.lcm_apply(lcm, self, lhs)

        return Fraction(lhs.top - self.top, self.bottom)

    def __mul__(self, rhs):
        """ overloads * """
        if isinstance(rhs, int):
            rhs = Fraction(rhs, 1)
        elif isinstance(rhs, float):
            return self.to_float() * rhs

        return Fraction(self.top * rhs.top, self.bottom * rhs.bottom)

    def __rmul__(self, rhs):
        """ overloads * but backwards """
        return self.__mul__(rhs)

    def __truediv__(self, rhs):
        """ overloads / """
        if isinstance(rhs, int):
            rhs = Fraction(rhs, 1)
        elif isinstance(rhs, float):
            return self.to_float() / rhs

        return Fraction(self.top * rhs.bottom, self.bottom * rhs.top)

    def __rtruediv__(self, lhs):
        """ overloads / but backwards """
        if isinstance(lhs, int):
            lhs = Fraction(lhs, 1)
        elif isinstance(lhs, float):
            return lhs / self.to_float()

        return Fraction(self.bottom * lhs.top, self.top * lhs.bottom)

    def simplify(self):
        """ simplifies the fraction """
        gcd = self.gcd(self.top, self.bottom)
        if not gcd == max(abs(self.top), abs(self.bottom)):
            self.top = int(self.top/gcd)
            self.bottom = int(self.bottom/gcd)

    def lcm(self, a, b):
        """ calculates lcm """
        return (a*b)/self.gcd(a,b)

    def gcd(self, first, second):
        """ gets gcd from first and second number """
        if second == 0:
            return first
        return self.gcd(second, first % second)

    def lcm_apply(self, lcm, *argv):
        """ applies the lcm """
        for fraction in argv:
            if lcm == fraction.bottom:
                continue
            fraction.top *= int(lcm/fraction.bottom)
            fraction.bottom = lcm

    def to_float(self):
        return self.top/self.bottom


def strip_mult(*args):
    temp = []
    for element in args:
        temp.append(element.strip())

    return temp


def parse(*args):

    message = 0
    inputs = []

    for index, input_ in enumerate(args):

        if input_.isdigit():
            inputs.append(int(input_))
            message = 1
        else:
            try:
                inputs.append(float(input_))
                message = 1
            except ValueError:
                fraction = []
                input_ = input_.split("/")
                if input_[1] == 0:
                    return "zero d", 0, 0
                for number in input_:
                    fraction.append(int(number.strip()))
                inputs.append(Fraction(fraction[0], fraction[1]))
                message = 1
            else:
                message = str(index)

    return message, inputs[0], inputs[1]


def main():
    # main function

    # print instrustion and get input 
    print("Fraction Calculator 1.0. Input a int, decimal, or fraction and the operator")
    # first_input = input("First Fraction: ")
    # operator = input("Operator (+, - , *, /): ")
    # second_input = input("Second Fraction: ")
    
    first_input = "2"
    operator = "/"
    second_input = "32/7"

    # unpack the strings
    first_input, operator, second_input = strip_mult(first_input, operator, second_input)
    message, first_input, second_input = parse(first_input, second_input)

    # if parsing did not worked, print error and break
    if not message:
        print(f"The #{message} fraction or float failed to be parsed")
        return 0
    elif message == "zero d":
        print("The denomincator of the fraction cannot be 0")
        return 0

    # switch statement to check operator
    try:
        if operator == "+":
            print(f"{first_input} + {second_input} = {first_input + second_input}")
        elif operator == "-":
            print(f"{first_input} - {second_input} = {first_input - second_input}")
        elif operator == "*" or operator == "x":
            print(f"{first_input} * ({second_input}) = {first_input * second_input}")
        elif operator == "/":
            print(f"{first_input} / ({second_input}) = {first_input / second_input}")
    except:
        print("Your input was not recognized, please try again")

    return 0


# system calls main
if __name__ == "__main__":
    main()