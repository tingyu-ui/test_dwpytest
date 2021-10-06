#!/usr/bin/env python
# -*- coding:utf-8 -*-
from requests import test_requests1


class TestApiRequest(TestCase):
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo1.txt",
        "headers": None,
        "encoding": "base64"
    }
    def test_send(self):
        ar = test_requests1.ApiRequest()
        print(ar.send(self.req_data))

