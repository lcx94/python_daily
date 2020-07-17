# -*- coding:utf-8 _*-
'''
@author: lcx
@file: print_in_order.py
@time: 2020/7/17 9:53
@desc:
Suppose we have a class:
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads.
Thread A will call first(), thread B will call second(), and thread C will call third().
Design a mechanism and modify the program to ensure that second() is executed after first(),
and third() is executed after second().
'''
import threading


class Foo:
    def __init__(self):
        self.condition = threading.Condition()
        self.count = 1

    def first(self, printFirst):
        with self.condition:
            while self.count != 1:
                self.condition.wait()
            printFirst()
            self.count = 2
            self.condition.notify_all()

    def second(self, printSecond):
        with self.condition:
            while self.count != 2:
                self.condition.wait()
            printSecond()
            self.count = 3
            self.condition.notify_all()

    def third(self, printThird):
        with self.condition:
            while self.count != 3:
                self.condition.wait()
            printThird()
            self.count = 1
            self.condition.notify_all()

    def printFirst(self):
        print('first')


if __name__ == '__main__':
    foo = Foo()
    foo.