class Vscode:
    def compiling(self):
        print("Compiling...")
        print("Executing...")


class Pycharm:
    def compiling(self):
        print("Spell check...")
        print("Compiling...")
        print("Executing...")


class fun:
    def duck(self, obj):
        obj.compiling()


p = Pycharm()
f = fun()
vs = Vscode()

f.duck(p)
f.duck(vs)