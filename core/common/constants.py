import os
import platform


class GlobalConstants(object):
    drivers_path = "resources\drivers"
    PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    CHROME_DRIVER_WIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "chromedriver.exe"))
    CHROME_DRIVER_LIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "chromedriver"))
    FIREFOX_DRIVER_WIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "geckodriver.exe"))
    FIREFOX_DRIVER_LIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "geckodriver"))
    OPERA_DRIVER_WIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "operadriver.exe"))
    OPERA_DRIVER_LIN = os.path.join(PROJECT_ROOT_DIR, os.path.join(drivers_path, "operadriver"))
    PLATFORM_NAME = platform.system()
    SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT_DIR, os.path.join("screenshots"))
