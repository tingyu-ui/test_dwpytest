#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml
from appium import webdriver

from UIautomation.page.base_page import BasePage
from UIautomation.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        #复用，不在初始化
        if self._driver is None:
            #字典
            caps = dict()
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            # 防止清空缓存，比如登陆信息
            caps["noReset"] = True
            #udid可以理解为公共变量,打开yaml,然后提取caps,udid
            caps["udid"] = yaml.safe_load(open("../page/configuration.yaml"))['caps']['udid']

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(10)

        return self

    #定义一个返回类型
    def main(self) ->Main:
        return Main(self._driver)
