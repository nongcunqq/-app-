from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

server = 'http://localhost:4723/wd/hub'
desires_caps = {
"platformName": "Android",
  "deviceName": "192.168.1.138:5555",
  "appPackage": "com.luojilab.player",
  "appActivity": "com.luojilab.business.HomeTabActivity ",
  "noReset": True,
  "unicodeKeyboard": True,
  "resetKeyboard": True,

}
driver = webdriver.Remote(server, desires_caps)
wait = WebDriverWait(driver,30)


time.sleep(1)
el2 = driver.find_element_by_xpath("//android.widget.TextView[@text='电子书']") #电子书
el2.click()



while True:
            # 当前页面显示的所有状态
            # items = wait.until(
            #     EC.presence_of_all_elements_located(
            #         (By.XPATH, '//*[@resource-id="com.tencent.mm:id/ep4"]//android.widget.FrameLayout')))
            # 上滑
            try:
                driver.swipe(100, 986, 100, 100, 586)
                print(2222222222)

            except:
                pass