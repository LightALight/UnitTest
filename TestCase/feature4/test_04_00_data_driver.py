#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @File    : test_04_00_data_driver.py

"""
测试特性:

-----------------------------------------------------
测试思路:
    进行所有队列的排列组合，去掉不符合条件

测试结果:
    pass:
    failed:
-----------------------------------------------------
"""

import unittest
from Resource.common_init import common_init
from TestCase.feature4.testdata import various as test_data
import ddt
import logging


env_value = "beta"
case_level = 5
time_out = 5  # unix才能使用
filter_env = "unknow"

if env_value == "alpha":
    from Variables.alpha import *
elif env_value == "beta":
    from Variables.beta import *
else:
    from Variables.gamma import *


@ddt.ddt
class test_04_00_checkparameter(unittest.TestCase):
    """测试验证"""

    @classmethod
    def setUpClass(cls):
        common_init.setUpClass()
        logging.basicConfig(
            filename='../logs/' + __name__ + '.log',
            format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
            level=logging.DEBUG,
            filemode='a',
            datefmt='%Y-%m-%d%I:%M:%S %p')

    @unittest.skipIf(0 > case_level, "过滤leve0用例.")
    @unittest.skipIf(filter_env == "prod", "过滤leve0用例.")
    # @timeout_decorator.timeout(seconds=time_out)
    @ddt.data(*test_data.testdata_level_0)
    def test_parameter_0(self, dict):
        """参数化
        """
        logging.debug("123")
        # time.sleep(5)
        print(dict.get("testcase"))
        print(baidu_url)
        self.assertEqual(dict.get("input_iphone"), dict.get("verfy_iphone"))

    @unittest.skipIf(1 > case_level, "过滤leve1用例.")
    @ddt.data(*test_data.testdata_level_1)
    def test_parameter_1(self, dict):
        """参数化
        """
        print(dict.get("testcase"))
        self.assertEqual(dict.get("input_iphone"), dict.get("verfy_iphone"))


if __name__ == "__main__":
    unittest.main()
