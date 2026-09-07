def calculate(expression):
    return eval(expression)


if __name__ == "__main__":
    user_input = input("Enter expression: ")
    result = calculate(user_input)
    print("Result:", result)
