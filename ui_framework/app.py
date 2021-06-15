#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver

from ui_framework.base_page import BasePage
from ui_framework.page.index_page import IndexPage


class App(BasePage):

    #app启动

    def start(self):
        if self.driver == None:
            print("driver == None, 创建driver")
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            #防止清空缓存，比如登陆信息
            caps["noReset"] = "true"
            #最重要的一步，与server建立链接
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            print("复用driver")
            self.restart()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        #页面入口
        return IndexPage(self.driver)
