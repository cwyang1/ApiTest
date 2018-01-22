# -*- coding: utf-8 -*-
import requests
import json
import unittest


class test_web1(unittest.TestCase):
    def test1(self):
        data_1 = {}
        url = "https://mlc.vip.com/mobile/common/getUserLogin"
        data=''
        headers=''
        respons1 = requests.get(url, data=data,headers=headers)

        json1 = respons1.text
        dict1 = json.loads(json1)
        # print(dict1["code"])
        self.assertEqual(dict1["code"], 1)

    def test2(self):
        data_1 = {}
        url = "https://mlc.vip.com/mobile/common/getUserLogin"
        r_1 = requests.get(url, data_1)

        json1 = r_1.text
        dict1 = json.loads(json1)
        print "返回数据: " ,json1
        print dict1["code"]
        self.assertEqual(dict1["code"], 1)

