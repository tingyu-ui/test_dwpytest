#!/usr/bin/env python
# -*- coding:utf-8 -*-
#雪球首页page
#可以直接继承basepage，调用已经封装好的UI操作
import yaml

from ui_framework.base_page import BasePage


class IndexPage(BasePage):
    def goto_market(self):
        #xpath等同于By.xpath
        # self.find("xpath", "//*[@text='行情']").click()

        # print(data)
        #data格式 {'-action': 'click', 'by': 'xpath', 'value': "//*[@text='行情']"}}
        #函数名：[{'action': ,'by': ,'value':, {}, {}}]
        #使用steps函数取出所有step
        # steps = data.get("goto_market")
        self.run_steps("../page/index_page.yaml", "goto_market")


