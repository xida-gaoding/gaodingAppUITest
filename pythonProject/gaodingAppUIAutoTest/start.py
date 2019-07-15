from CommonTestRunner import *
from conf.config import *

if __name__ == '__main__':
    runner = CommonTestRunner()
    device = ["Android://127.0.0.1:5037/7366daaa"] # 如何动态获取多个设备，并并行运行多个air
    runner.run_air( get_air_path(), device, get_log_path() )