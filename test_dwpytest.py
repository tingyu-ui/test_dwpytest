#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()


    def test_search(self):
        print("搜索测试用例")
        """
        1.打开需求app
        2.点击搜索输入框
        3.向索搜输入框输入“阿里巴巴”
        4.在搜索结果里选择“阿里巴巴”，然后点击
        5.获取阿里巴巴的股价，并判断，这只股票的价格>200
        
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        time.sleep(6)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)

        assert current_price > 200


    def test_attr(self):
        """

        :return:
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        #判断搜索框是否可用
        # print(element.is_enabled())
        search_enabled = element.is_enabled()
        #查看搜索框name属性
        print(element.text)
        #打印xy坐标
        print(element.location)
        #打印坐标宽高
        print(element.size)
        #如果索搜框状态=true，那么就点击click
        if search_enabled == True:
            element.click()
            #向索搜框输入alibaba
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # print(alibaba_element.get_attribute("displayed"))
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")
    #触屏操作自动化
    def test_touchaction(self):
        action = TouchAction(self.driver)
        #打印xy坐标值
        # print(self.driver.get_window_rect())
        #因为坐标尺寸容易变化，所以不建议使用
        # action.press(x=710,y=1083).wait(200).move_to(x=710,y=484).release().perform()
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        current_price = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前09988 对应的股票价格是：{current_price}")
        assert float(current_price) > 200

    def test_myinfo(self):
        """
        1,点击我的，进入到个人信息页面
        2，点击登陆，进入到登陆页面
        3，输入用户名，输入密码
        4，点击登陆
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        # self.driver.page_source()
        # self.driver.implicitly_wait(10)
        # newCommandTimeout:"3000"
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码登陆")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resonrceId("com.xueqiu.android:id/login_password")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")')

        #滚动查找
    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("雪盈证券").'
                                                        'instance(0));').click()
        time.sleep(5)


if __name__ == '__main__':
    pytest.main()
