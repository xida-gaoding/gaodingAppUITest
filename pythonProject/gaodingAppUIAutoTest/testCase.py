# -*- encoding=utf8 -*-
__author__ = "Administrator"
from airtest.core.api import *
auto_setup( __file__ )
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
class TestCase:
    poco = AndroidUiautomationPoco( use_airtest_input=True, screenshot_each_action=False )
    def __init__(self):
        connect_device("Android:///")  # 连接设备
        start_app( "com.hlg.daydaytobusiness" )
        sleep( 5 )
    #功能：切换比例保存图片：
    #步骤：首页点击图片标记--滑动相册页--点击一张图片--点击制作--点击编辑--切换比例3：4--点击完成--点击保存--验证保存成功--点击返回首页
    def switchRatioAndSavePhoto(self):
        self.poco( text="图片标记" ).click()
        self.poco.swipe( [0.5, 0.7], [0.5, 0.3] )
        sleep( 5 )
        self.poco.click( [0.4, 0.4] )
        self.poco( text="制作" ).click()
        self.poco( text="编辑" ).click()
        self.poco( text="3:4" ).click()
        self.poco( text="完成" ).click()
        self.poco( text="保存" ).click()
        assert_exists(Template(r"tpl1562829085071.png", record_pos=(0.015, -0.099), resolution=(1080, 2160)), "切换比例测试")
        self.poco( text="返回首页").click()
    #功能：添加马赛克保存图片：
    #步骤：首页点击图片标记--滑动相册页--点击一张图片--点击制作--点击马赛克--滑动图片添加马赛克--点击完成--点击保存--验证保存成功--点击返回首页
    def addWordsAndSavePhoto(self):
        poco = AndroidUiautomationPoco( use_airtest_input=True, screenshot_each_action=False )
        sleep( 5 )
        poco( text="图片标记" ).click()
        poco.swipe( [0.5, 0.7], [0.5, 0.3] )
        sleep( 5 )
        poco.click( [0.4, 0.4] )
        poco( text="制作" ).click()
        poco( text="马赛克" ).click()
        poco.swipe( [0.5, 0.7], [0.5, 0.3] )
        sleep( 5 )
        self.poco( text="完成" ).click()
        self.poco( text="保存" ).click()
        assert_exists(Template(r"tpl1562829085071.png", record_pos=(0.015, -0.099), resolution=(1080, 2160)), "切换比例测试")
        self.poco( text="返回首页").click()






