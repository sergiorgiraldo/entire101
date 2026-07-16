def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    x = float(input("First number: "))
    y = float(input("Second number: "))
    op = input("Operation (+/-/*): ")
    if op == "-":
        print("Result:", subtract(x, y))
    elif op == "*":
        print("Result:", multiply(x, y))
    else:
        print("Result:", add(x, y))
