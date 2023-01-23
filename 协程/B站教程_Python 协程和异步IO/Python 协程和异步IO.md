# Python 协程和异步IO

B站地址：[Python 协程和异步IO_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1vE411F7Z9/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=eef98f9e120e9dac4c55f6547f221385)



## 1. 协程简介



## 2.yield的使用

有yield的函数会成为生成器函数

把yield看作是return

res=yield 4

先用next方法激活（不能给尚未激活的生成器函数发值），函数会运行到第一个yield处停留（只完成了yield右侧部分，左侧赋值等待下个send或者next方法）

如果使用next（.__next__)方法继续调用，res为None，函数运行到下一个yield右侧，或者程序结束返回stopiteration错误

如果使用send方法继续调用，res为send的参数，函数运行到下个yield右侧，或者程序结束返回stopiteration错误



## 3.yield实现生产者和消费者

使用send函数可以向协程函数发送数据

在生产者和消费者这个案例中，消费者是一个生成器函数，生产者是一个参数为生成器函数的函数。将逻辑中的后手设定为生成器函数，先手设定为带生成器函数参数的函数

