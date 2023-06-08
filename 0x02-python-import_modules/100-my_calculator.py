#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, op, b = sys.argv[1:]

    if op == "+":
        result = int(a) + int(b)
    elif op == "-":
        result = int(a) - int(b)
    elif op == "*":
        result = int(a) * int(b)
    elif op == "/":
        result = int(a) / int(b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, result))
