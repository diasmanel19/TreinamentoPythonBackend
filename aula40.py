# Decorators

def estudo(func):
    def wrapper():
        print("estou começando a estudar...")
        func()
        print("estou terminando de estudar...")
        func()
    return wrapper


@estudo
def linguagem():
    print("python")

linguagem()