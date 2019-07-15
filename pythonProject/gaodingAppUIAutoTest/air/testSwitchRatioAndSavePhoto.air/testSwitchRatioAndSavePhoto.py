# -*- encoding=utf8 -*-
from airtest.core.api import *
__author__ = "Administrator"
auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#功能：切换比例保存图片：
#步骤：首页点击图片标记--滑动相册页--点击一张图片--点击制作--点击编辑--切换比例3：4--点击完成--点击保存--验证保存成功--点击返回首页
# def switchRatioAndSavePhoto(self):
#     poco( text="图片标记" ).click()
#     poco.swipe( [0.5, 0.7], [0.5, 0.3] )
#     sleep( 5 )
#     poco.click( [0.4, 0.4] )
#     poco( text="制作" ).click()
#     poco( text="编辑" ).click()
#     poco( text="3:4" ).click()
#     poco( text="完成" ).click()
#     poco( text="保存" ).click()
#     assert_exists(Template(r"tpl1562829085071.png", record_pos=(0.015, -0.099), resolution=(1080, 2160)), "切换比例测试")
#     poco( text="返回首页").click()
poco( text="图片标记" ).click()
poco.swipe( [0.5, 0.7], [0.5, 0.3] )
sleep(5)
poco.click( [0.4, 0.4] )
poco( text="制作" ).click()
poco( text="编辑" ).click()
poco( text="3:4" ).click()
poco( text="完成" ).click()
poco( text="保存" ).click()
assert_exists(Template(r"tpl1562829085071.png", record_pos=(0.015, -0.099), resolution=(1080, 2160)), "切换比例测试")
poco( text="返回首页").click()