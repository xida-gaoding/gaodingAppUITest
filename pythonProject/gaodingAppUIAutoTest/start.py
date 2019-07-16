
from conf.config import *
from CommonTestRunner import *

from gaodingAppUIAutoTest.CommonTestRunner import *
from gaodingAppUIAutoTest.conf.config import *


if __name__ == '__main__':
    runner = CommonTestRunner()
    for device in getFixedAndroidDevices():
        runner.run_air( get_air_path(), device, get_log_path())
