# функция-декоратор
def dec(func_arg):
    def wrapper():
        print("Before")
        func_arg()
        print("After")
    return wrapper

# целевая функция
@dec
def func_1():
    print ("Hello!")

func_1()