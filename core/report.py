# -*- coding: utf-8 -*-
#防中文乱码
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#依赖
import requests
import json
import os
import unittest
from api_suit import test_web1
from HTMLTestRunner import HTMLTestRunner
import time
from apitest_lists import test_lists


if __name__ == '__main__':
    #定义脚本标题，加u为了防止中文乱码
    report_title = u'测试报告'

    #定义脚本内容，加u为了防止中文乱码
    desc = u'接口自动化测试报告详情：'

    #定义date为日期，time为时间
    date=time.strftime("%Y%m%d")
    time=time.strftime("%Y%m%d%H%M%S")

    #定义path为文件路径，目录级别，可根据实际情况自定义修改
    # path= 'D:/Python_test/'+ date +"/login/"+time+"/"
    path= 'D:/Python_test/'+ date +"/"

    #定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    report_path = path+time+".html"

    #判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    #定义一个测试容器
    api_suite = unittest.TestSuite()

    api_suite.addTests(test_lists)

    #将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(api_suite)

    #关闭report，脚本结束
    report.close()

