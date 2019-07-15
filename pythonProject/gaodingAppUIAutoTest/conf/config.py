#-*- coding: utf-8 -*
import os
Androiddevice=["Android://127.0.0.1:5037/172.16.12.131:5555"]#连接安卓设备127.0.0.1:5037固定写法172.16.81.115安卓真机的Ip

def get_air_path():
    return os.path.join(getProjectPath(),'air')
def get_log_path():
    return os.path.join(getProjectPath(),'log')
def get_report_path():
    return os.path.join(getProjectPath(),'report')
def get_data_path():
    return os.path.join(getProjectPath(),'data')

def getProjectPath():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.dirname(path)
    return path