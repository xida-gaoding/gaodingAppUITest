# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
start_app("com.hlg.daydaytobusiness")
sleep(5)
poco(text="图片标记").click()
poco.swipe([0.5,0.7],[0.5,0.3])
poco.click([0.7,0.4])
poco(text="制作").click()
poco(text="马赛克").click()
poco.swipe([0.5,0.7],[0.5,0.3])
poco(text="完成").click()
poco(text="保存").click()
assert_exists(Template(r"tpl1562829085071.png", record_pos=(0.015, -0.099), resolution=(1080, 2160)), "切换比例测试")
poco(text="返回首页").click()






