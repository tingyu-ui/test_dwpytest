#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestSearch:
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "android"
        desired_caps["platformVersion"] = '6.0'
        #当只有一台设备时这个名字随便取都可以找到，但是有多台时名字不是唯一标识
        # desired_caps["deviceName"] = 'emulator-5554'
        #所以需要用udid来确认唯一性
        # desired_caps["udid"] = 'emulator-5554'
        #自动点击弹框
        # desired_caps["autoGrantPermissions"] = True
        #不让设备停止app
        desired_caps["dontStopAppOnReset"] = True
        desired_caps["appPagekage"] = 'com.xueqiu.android'
        desired_caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
        # desired_caps["noReset"] = True
        desired_caps["unicodeKeyBoard"] = 'True'
        desired_caps["resetKeyBoard"] = 'True'
        #提前创建好的模拟器，自动启动
        desired_caps["avd"] = 'Pixel_2_XL_API_23'
        #设备在300秒内都不会报异常
        desired_caps["newCommandTimeout"] = 300
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_mobile(self):
        #模拟来电话
        # self.driver.make_gsm_call('13011112222', GsmCallActions.CALL)
        #
        # #模拟来短信
        # self.driver.send_sms('13100001111', 'hello appium api')
        #录屏
        # self.driver.start_recording_screen()
        #模拟网络0:什么网络信号都没有，1：飞行模式；2：wifi模式；4：移动数据模式；6：移动数据及wifi模式全开
        self.driver.set_network_connection(1)
        sleep(5)
        #5秒后设置为4数据模式
        self.driver.set_network_connection(4)
        sleep(3)

        #截屏 android 8.0以上才支持，并且华为手机不支持
        self.driver.get_screenshot_as_file('./photos/img.png')

        #停止录屏,android 8.0以上才支持，并且华为手机不支持
        # self.driver.stop_recording_screen()