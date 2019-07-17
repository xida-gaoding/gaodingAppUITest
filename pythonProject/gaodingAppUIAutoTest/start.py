#from CommonTestRunner import *
from conf.config import *
from utils.Utils import *
import multiprocessing as mp
from airtest.core.android.adb import ADB
from MultiDeviceRunner import *

utils = Utils()
def runMultiDevices():
    devices = [tmp[0] for tmp in ADB().devices()]
    """"
    TODO：
    1. 遍历air路径，
    2. 整合报告，通过air来命名或者多个整合成一个报告
    3. 理清结构和整个流程，data.json,report_tpl.html,report.html,关系和作用
    4. 源码分析，多设备多进程如何实现，task，
    
    """
    # 对获取的设备放入到字典中，取出字典的第一个值
    devices = [tmp[0] for tmp in ADB().devices()]
    airList = utils.getAirList()
    for air in airList:
        # 获取到的air添加路径上一级路径，因为run.py把air用例放到工程目录下，而当前框架是把air用例统一放到air目录下
        newair = "air\\" + air
        print(newair)
        run(devices, newair, run_all=True)

if __name__ == '__main__':
    runMultiDevices()
    # runner = CommonTestRunner()
    # devices = [tmp[0] for tmp in ADB().devices()]
    #
    # tasks = runner.run_on_multi_device(devices,get_air_path())
    # for task in tasks:
    #     status = task['process'].wait()
#    for device in utils.getFixedAndroidDevices():
         # runner.run_air( get_air_path(), device, get_log_path())
         # p1 = mp.Process(target=runner.run_air, args=(get_air_path(), device))
         # p1.start()



