#-*- coding: utf-8 -*
#Androiddevice=["Android://127.0.0.1:5037/172.16.12.131:5555"]#连接安卓设备127.0.0.1:5037固定写法172.16.81.115安卓真机的Ip
#获取完整的安卓设备信息
#from gaodingAppUIAutoTest.utils.Utils import *
import sys
import os

#获取air路径
def get_air_path():
    return os.path.join(getProjectPath(),'air')
#获取log路径
def get_log_path():
    return os.path.join(getProjectPath(),'log')
#获取report路径
def get_report_path():
    return os.path.join(getProjectPath(),'report')
#获取data路径
def get_data_path():
    return os.path.join(getProjectPath(),'data')

#获取工程目录
def getProjectPath():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.dirname(path)
    return path