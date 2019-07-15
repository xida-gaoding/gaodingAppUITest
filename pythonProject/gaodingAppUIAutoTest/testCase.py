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
    def addMasaicAndSavePhoto(self):
        self.poco( text="图片标记" ).click()
        self.poco.swipe( [0.5, 0.7], [0.5, 0.3] )
        sleep( 5 )
        self.poco.click( [0.4, 0.4] )
        self.poco( text="制作" ).click()
        self.poco( text="马赛克" ).click()
        self.poco.swipe( [0.5, 0.7], [0.5, 0.3] )
        sleep( 5 )
        self.poco( text="完成" ).click()
        self.poco( text="保存" ).click()
        assert_exists(Template(r"tpl1562829085071.png", record_pos=(0.015, -0.099), resolution=(1080, 2160)), "切换比例测试")
        self.poco( text="返回首页").click()
    #判断是否登录，未登录返回False，已登录返回True
    def isLogin(self):
        self.poco( text = "账号" ).click()
        loginResult = self.poco("b'com.hlg.daydaytobusiness:id/tv_persion_name'").get_text()
        if loginResult == "未登录":
            return False
        else:
            return True
    #未登录状态，执行登录操作--微信注册
    #步骤：点击账号--点击未登录--点击微信--判断微信是否注册--未注册--点击注册--手机绑定
    def logonByWechatOfUnregistered(self):
        if self.isLogon() == False:
            self.poco( text = "未登录" ).click()
            #点击微信图标
            touch(Template(r"tpl1563162248095.png", record_pos=(-0.279, 0.781), resolution=(1080, 2160)))
            self.poco( text = "继续注册").click()
            #手机绑定
            self.poco( text = "输入手机号码" ).click()
            text("18250201690")
            #输入验证码
            self.poco( text = "获取验证码").click()
            self.poco("b'com.hlg.daydaytobusiness:id/et_verify'").click()
            text("123456")
            #输入密码
            self.poco("b'com.hlg.daydaytobusiness:id/et_regist_password'").click()
            text("123456")
            #点击完成注册
            self.poco("完成注册").click()
            #待验证
        else:
            log("账号已登录")
    #未登录状态，执行登录操作--微信登录（账号已注册）
    #步骤：点击账号--点击未登录--点击微信--判断微信是否注册--未注册--点击注册--手机绑定
    def logonByWechatOfRegistered(self):
        if self.isLogin() == False:
            self.poco( text = "未登录" ).click()
            #点击微信图标
            touch(Template(r"tpl1563162248095.png", record_pos=(-0.279, 0.781), resolution=(1080, 2160)))
            sleep(2)
            userName = self.poco(b'com.hlg.daydaytobusiness:id/tv_persion_name').get_text()
            assert_not_equal(str(userName),"未登录","验证账号名不是未登录")


if __name__ == "__main__":
    testcase = TestCase()
    # testcase.switchRatioAndSavePhoto()
    # testcase.addMasaicAndSavePhoto()
    print("是否登录："+str(testcase.isLogin()))
    testcase.logonByWechatOfRegistered()










