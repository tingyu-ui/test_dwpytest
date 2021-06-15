#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest as pytest
import yaml

from page.app import App
from test_case.test_base import TestBase


class TestMain(TestBase):
    #参数化
    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("./test_main.yaml")))
    def test_main(self, value1, value2):
        # app = App()
        self.app.start().main().goto_search()
        #打印，确认是否真的加载进来
        print(value1)
        print(value2)

    def test_windows(self):
        # app = App()
        self.app.start().main().goto_windows()
