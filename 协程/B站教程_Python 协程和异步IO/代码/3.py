# 使用yield实现生产者消费者

def producer():
    while True:
        res = yield 42
        print('res:',res)

def consumer(p):
    for i in range(3):
        p.send(i)
        # print(i,'consumer',next(p))
        
p=producer()
next(p)
consumer(p)
    

