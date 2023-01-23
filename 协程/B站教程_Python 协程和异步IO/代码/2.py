#2.yield的使用

#yield的理解
def foo():
    print("Starting")
    while True:
        res = yield 4
        print('res:', res)


g = foo()
print(type(g))
print(next(g))
print(next(g))
print(next(g))


#一个简单的协程
def A(b):
    for i in range(3):
        print('A')
        print(next(b))

def B():
    while True:
        yield 'B'

b=B()
next(b)
A(b)

