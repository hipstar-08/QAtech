import os

from core.common.constants import GlobalConstants


def capture_screenshot(driver, screenshot_path=os.path.join(GlobalConstants.SCREENSHOTS_DIR, "screenshot.png")):
    driver.save_screenshot(screenshot_path)
