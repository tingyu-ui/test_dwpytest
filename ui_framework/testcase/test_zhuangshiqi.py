#!/usr/bin/env python
# -*- coding:utf-8 -*-
#装饰器最重要的功能 增强已有功能的函数
#a 是最基础函数，就相当于框架中的find方法
#如果想对a进行增强的话，可以直接向a中添加代码
#问题：如果功能越来越多，每个功能代码都写在a函数中的话，a代码就会越来越多，find方法也是同样的问题
#解决：如果不改动a代码，对a进行功能增强
def a():
    print("hello")
    print("我是A")
    print("good bye")

#装饰器定义B
#1，定义装饰器，可以是函数，也可以是类，比如下面代码定义了装饰器b,b的名字可以随便取
#2,b的参数是被装饰的对象
#3，在b中要声明一个函数，函数的名字随便取，但是一定要和retrun的值一样，比如函数的名字是C,return的值也是c
#4,如何使用装饰器，详见c代码
#5，如果装饰的是c,那么fun是c,不是c(),
def b(fun):
    def d():
        print("hello")
        #python中加了（）才表示调用
        fun()
        print("good bye")

    return d

#优化 增加装饰器@b
#1,装饰器 要使用@ 符号进行调用，比如@b装饰器
@b
def c():
    # print("hello")
    # print("我是c")
    # print("good bye")
    print("我是c")
@b
def d():
    # print("hello")
    # print("我是c")
    # print("good bye")
    print("我是d")

#调用
def test_a():
    d()


def f()
    print("我 是f")
#不加括号的是函数ID,相当于叫了一声小明
#加了括号，代表调用函数，相当于让小明去帮忙买水
def test_f():
    f
    f()