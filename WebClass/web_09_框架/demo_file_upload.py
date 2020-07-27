import time

from selenium import webdriver

driver = webdriver.Chrome()

url = "file:///D:/%E7%8F%AD%E7%BA%A7%E7%AE%A1%E7%90%86/python28%E6%9C%9F/web_09_%E6%A1%86%E6%9E%B6/demo.html"
driver.get(url)

# 定位元素
mfile_elem = driver.find_element("name", "mfile")

# 发送文件和发送文字是一样的，都是 send_keys
# send_keys(文本，键盘，文件路径)
# 不需要执行点击操作，input

# mfile_elem.send_keys(r"d:\demo.txt")

time.sleep(3)
# 点击上传文件的窗口
mfile_elem.click()

# 上传操作 pywinauto
# from pywinauto import Desktop
# app = Desktop()
# # 窗口
# dialog = app['打开']    #根据名字找到弹出窗口
# # 窗口上的控件
# time.sleep(1)
# dialog["Edit"].type_keys(r"d:\demo.txt")     # 在输入框中输入值
# dialog["Button"].click()

# linux, mac  pyautogui
import pyautogui
pyautogui.write('d:\demo.txt')
# 速度太快
pyautogui.press('enter', 2)

time.sleep(3)


# 定位第二个上传位置
mfile = driver.find_element("name", "AnotherFile")
# 点击
mfile.click()
# 发送文件
from pywinauto import Desktop
app = Desktop()
# 窗口
dialog = app['打开']    #根据名字找到弹出窗口
# 窗口上的控件
time.sleep(1)
dialog["Edit"].type_keys(r"d:\demo2.txt")     # 在输入框中输入值
dialog["Button"].click()

time.sleep(2)


# 发送中文
# import pyperclip
# pyperclip.copy('D:\用户.html')
#
# time.sleep(2)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.press('enter', presses=2)


