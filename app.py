import subprocess

PASSWORD = "admin123"


def calculate(expression):
    return eval(expression)


def run_command(command):
    return subprocess.call(command, shell=True)


if __name__ == "__main__":
    user_input = input("Enter expression: ")
    result = calculate(user_input)
    print("Result:", result)
