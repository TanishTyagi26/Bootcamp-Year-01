#Create a fn. make_operator(op) that return a lambda fn. based on the string op (+,-,*,/).
#call it to create add ,sub, multiply, divide fns and test each with two numbers




def make_operator(op):

    if op == "+":
        return lambda a, b: a + b

    elif op == "-":
        return lambda a, b: a - b

    elif op == "*":
        return lambda a, b: a * b

    elif op == "/":
        return lambda a, b: a / b

    else:
        return lambda a, b: "Invalid Operator"


add = make_operator("+")
sub = make_operator("-")
multiply = make_operator("*")
divide = make_operator("/")

print("Addition :", add(10, 5))
print("Subtraction :", sub(10, 5))
print("Multiplication :", multiply(10, 5))
print("Division :", divide(10, 5))