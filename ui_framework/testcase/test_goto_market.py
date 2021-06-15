#!/usr/bin/env python
# -*- coding:utf-8 -*-
from ui_framework.app import App


class TestGotoMarket:
    def setup(self):
        #生成appium的实例并传给后面的page类
        self.app = App().start()


    def test_go_to_market(self):
        self.app.goto_main().goto_market()
