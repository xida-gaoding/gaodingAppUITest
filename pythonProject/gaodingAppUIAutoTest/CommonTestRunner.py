import traceback

from airtest.cli.runner import AirtestCase, run_script
from argparse import *
import shutil
from conf.config import *
#from lib.log import *
import logging
import os
import multiprocessing as mp
from airtest.report.report import simple_report
from airtest.core.api import *
from utils.Utils import *

from pythonProject.gaodingAppUIAutoTest.utils.Utils import Utils

auto_setup( __file__ )
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

utils = Utils()
class CommonTestRunner( AirtestCase ):  # 继承AirtestCase类

    def setUp(self):
        logging.info( "案例开始执行" )
        super( CommonTestRunner, self ).setUp()  # 继承父类的setup方法

    def tearDown(self):
        logging.info( "案例执行结束" )
        super( CommonTestRunner, self ).tearDown()  # 继承父类的tearDown方法



    # 本方法主要是查找脚本文件，目录文件，初始化AirtestCase所需要的参数，执行脚本，并生成报告
    def run_air(self, root_dir, device,logpath):
        dirs = os.listdir(root_dir)#获取root_dir路径下的文件
        print("run_air, dirs:" + str(dirs))
        for f in dirs:  # 循环查找air所在的目录
            if f.endswith( ".air" ):  # 以air结尾的文件
                airName = f
                script = os.path.join( root_dir, f )  # 脚本目录
                logging.info( script )
                deviceLogPath = utils.getDeviceLogPath()
                log = os.path.join(deviceLogPath + '\\' + airName.replace( '.air', str(utils.getCurrentTime()) ) )  # 日志目录
                logging.info( log )
                if os.path.isdir( log ):
                    shutil.rmtree( log )  # 清空日志目录文件
            else:
                os.makedirs( log )#创建日志目录
            args = Namespace( device=device, log=log, recording=None, script=script )  # 初始化父类AirtestCase所需要的参数
            try:
                run_script( args, AirtestCase )  # 执行air脚本文件
            except AssertionError:
                logging.info( "案例执行失败" )
#            finally:
#                output_file = get_report_path() + '\\' + airName.replace( '.air', utils.getCurrentTime() ) + '.html'  # 生成报告目录
#                simple_report( script, logpath=log, output=output_file )  # 生成报告的方法
#                logging.info( "案例执行成功" )


