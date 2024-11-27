class fun1:
    def __init__(self):
        print("First function of Base class")


class fun2:
    def __init__(self):
        print("Second function of Base class")


class fun3(fun1, fun2):
    def __init__(self):
        super().__init__()
        print("Functin of child class")


obj = fun3()
