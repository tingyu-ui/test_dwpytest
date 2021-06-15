#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    _driver: WebDriver
    #黑名单
    _black_list=[(By.ID, "iv_close")]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver
    #封装find方法
    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            #对黑名单进行遍历
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                #如果发现黑名单长度是大于0，那就对黑名单进行点击
                if len(elements) > 0:
                    elements[0].click()
                    #跳出循环
                    break
                #处理完黑名单后，再次找原来的元素
                return self.find(locator, value)
    #也可以根据自己项目来封装，比如click封装
    # def click(self, locator, value):
    #     #然后把value传进来
    #     self.find(locator, value).click()

    #封装steps
    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        #yaml解析
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            #如果action在step中，那就提取出action
            if "action" in step.keys():
                action = step["action"]
                #如果是点击操作，那就复用element
                if action == "click":
                    element.click()
