#yield的使用


def foo():
    print("Starting")
    while True:
        res = yield 4
        print('res:', res)


g = foo()
print(type(g))
print(next(g))
print(next(g))