def add(a, b):
    return a+b
def subt(a, b):
    return a - b
def multi(a, b):
    return a * b
def division(a, b):
    return a / b


if __name__ == "__main__":
    a,b = int(input("Введіть перше число ")), int(input("Введіть друге число "))
    c = input("Введіть дію ")
    if c == "+":
        res = add(a,b)
        print(f"Результат додавання:{res} ")
    elif c == "-":
        res1 =subt(a,b)
        print(f"Результат  віднімання:{res1} ")
    elif c == "*":
        res2 =multi(a,b)
        print(f"Результат  множення:{res2} ")
    elif c == "/":
        res3 =division(a,b)
        print(f"Результат  ділення:{res3}")