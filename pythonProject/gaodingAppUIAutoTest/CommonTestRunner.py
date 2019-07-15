from airtest.cli.runner import AirtestCase, run_script
from argparse import *
import shutil
from conf.config import *
#from lib.log import *
import logging
import os
from airtest.report.report import simple_report
from airtest.core.api import *

auto_setup( __file__ )
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class CommonTestRunner( AirtestCase ):  # 继承AirtestCase类
#    Androiddevice=["Android://127.0.0.1:5037/7366daaa"]#连接安卓设备127.0.0.1:5037固定写法172.16.81.115安卓真机的Ip

    def setUp(self):
        logging.info( "案例开始执行" )
        super( CommonTestRunner, self ).setUp()  # 继承父类的setup方法
        # connect_device( "Android:///" )  # 连接设备
        # start_app( "com.hlg.daydaytobusiness" )
        # sleep( 5 )

    def tearDown(self):
        logging.info( "案例执行结束" )
        super( CommonTestRunner, self ).tearDown()  # 继承父类的tearDown方法

    def run_air(self, root_dir, device,logpath):  # 本方法主要是查找脚本文件，目录文件，初始化AirtestCase所需要的参数，执行脚本，并生成报告
        dirs = os.listdir(root_dir)
        print("run_air, dirs:" + str(dirs))
        for f in dirs:  # 循环查找air所在的目录
            if f.endswith( ".air" ):  # 以air结尾的文件
                airName = f
                script = os.path.join( root_dir, f )  # 脚本目录
                logging.info( script )
                log = os.path.join(logpath + '\\' + airName.replace( '.air', '' ) )  # 日志目录
                logging.info( log )
                if os.path.isdir( log ):
                    shutil.rmtree( log )  # 清空日志目录文件
            else:
                os.makedirs( log )
            args = Namespace( device=device, log=log, recording=None, script=script )  # 初始化父类AirtestCase所需要的参数
            try:
                run_script( args, AirtestCase )  # 执行air脚本文件
            except AssertionError:
                logging.info( "案例执行失败" )
            finally:
#               output_file = log + '\\' + airName.replace( '.air', '' ) + '.html'
#                output_file = self.reportpath + '\\' + airName.replace( '.air', '' ) + '.html'  # 生成报告目录
#                simple_report( script, logpath=log, output=output_file )  # 生成报告的方法
                logging.info( "案例执行成功" )
#
# if __name__ == '__main__':
#     test = CommonTestRunner()
#     print( test.airpath )
#     device = ["Android://127.0.0.1:5037/7366daaa"] # 如何动态获取多个设备，并并行运行多个air
#     print( device)
#     test.run_air( get_air_path(), device )
