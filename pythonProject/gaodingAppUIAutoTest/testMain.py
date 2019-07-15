# -*- encoding=utf8 -*-
from testCase import *
# __author__ = "Administrator"
# from airtest.core.api import *
# auto_setup( __file__ )
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# print("测试不执行")
# if __name__ == "__main__":
testcase = TestCase()
testcase.switchRatioAndSavePhoto()
testcase.addWordsAndSavePhoto()
