import sys
sys.path.append("..")
import time
import os
import re
import sys
from airtest.core.android.android import *
from airtest.core.android.adb import *
from conf.config import *


class Utils:
    CMD_GETDEVICES = "adb devices"

    def getCurrentTime(self):
        return time.strftime("%Y%m%d%H%M%S", time.localtime())

    # 执行cmd命令获取字符串
    def execCMDAndgetStr(self, command):
        result = os.popen(command).read()
        return result

    # 判断是否连接设备，未连接返回False，连接返回true
    def isConnectDevices(self):
        if self.execCMDAndgetStr(self.CMD_GETDEVICES) == "List of devices attached\n\n":
            return False
        else:
            return True

    def getDevicesList(self):
        results = self.execCMDAndgetStr(self.CMD_GETDEVICES)
        # 如果只显示List of devices attached，则打印未连接设备
        if self.isConnectDevices() == False:
            print("未获取到设备，请确认是否连接设备")
            # 退出执行
            sys.exit()
        else:
            # 字符串获取有效的设备列表：去掉第一行24个字符，去掉\tdevices，去掉末尾空格，根据换行切割放入设备列表
            device_list = re.sub('\tdevice|\tunauthorized|\toffline', '', results[25:]).strip().split('\n')
            print(device_list)
            return device_list

    # 添加完整的设备信息
    # airtest的设备参数为["Android://127.0.0.1:5037/xxxx"]#连接安卓设备127.0.0.1:5037固定写法，xxx为安卓真机的Ip
    def getFixDevices(self, msg):
        fixedDevices = []
        devicesList = self.getDevicesList()
        for device in devicesList:
            device = msg + device
            fixedDevices.append(device)
        print(fixedDevices)
        return fixedDevices

    def getFixedAndroidDevices(self):
        fixedDevices = self.getFixDevices("Android://127.0.0.1:5037/")
        return fixedDevices

    # 判断是否安装测试包
    def isInstallTestPackage(self, device, testPackage):
        androidDevice = Android(device)
        try:
            isInstallApp = androidDevice.check_app(testPackage)
        except AirtestError:
            print("未安装设备")
            return False
        else:
            return True
        #设备未安装测试包，安装测试包
    def installApp(self,device,testPackage):
        if self.isInstallTestPackage() == False:
            androidDevice = Android(device)
            androidDevice.install_app(testPackage,device)


    def getDeviceLogPath(self):
        devicesList = self.getDevicesList()
        # 获取log路径
        # logPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'log')
        projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logPath = os.path.join(projectPath, "log")
        if os.path.exists(logPath):
            print("路径存在" + logPath)
            for device in devicesList:
                deviceLogPath = os.path.join(logPath, device)
                if not os.path.exists(deviceLogPath):
                    os.mkdir(deviceLogPath)
                else:
                    print("目录已存在")
        else:
            # todo
            os.makedirs(logPath)  # 创建日志目录
        return deviceLogPath


# utils = Utils()
# deviceslist = utils.getDevicesList()
# utils.getDevicesList()
# utils.getFixDevices("Android://127.0.0.1:5037/")
# utils.execCMDAndgetStr("adb devices")
# utils.getDevicesList()
# utils.isInstallTestPackage("GWY0217304000475","com.hlg.daydaytobusiness")
