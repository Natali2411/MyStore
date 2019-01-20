import random, time
import string


def test_123(reg):
    print("Browser was started")
    print("The main page was loaded")
    time.sleep(5)
    reg.wd.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a').click()
    time.sleep(3)
