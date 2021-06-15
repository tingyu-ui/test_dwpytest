#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        #yaml优化
        # self.find(By.ID, 'home_search').click()
        # self.find(By.ID, 'tv_search').click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        #先点击“笔”
        self.find(By.ID, "post_status").click()
        self.find(By.ID, "home_search").click()

