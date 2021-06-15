#!/usr/bin/env python
# -*- coding:utf-8 -*-

#基类，完成底层封装，比如常用的一些方法，初始化driver,find。。。
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
#日志打印
root=logging.getLogger()
print(root.handlers)
for h in root.handlers[:]:
    #将原有日志清空，重新加载
    root.removeHandler(h)


class BasePage:
    #日志,info级别的日志，需要大写
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver =None):
        self.driver = driver

    def find(self, by,value):
        #日志info小写
        logging.info(by)
        logging.info(value)
        return self.driver.find_element(by,value)
    #封装滑动查找3次
    def swipe_fine(self,text,num):
        # num = 3
        for i in range(0,num):
            if i == num-1:
                raise NoSuchElementException(f"找了{num-1}没有找到元素")
            try:
                return self.find(MobileBy.XPATH, f"//*[@text= '{text}']")
            except:
                print("未找到，滑动")
                #'width','height'
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                startx = width/2
                starty = height *0.8 #滑动到4/5处
                endx = startx
                endy = height * 0.3
                duration = 2000 #2秒
                self.driver.swipe(startx,starty,endx,endy,duration)