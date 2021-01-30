from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys

hwnd = win32gui.FindWindow(None, 'us4加速 - 173.82.153.248.ipssh.net:43389 - 远程桌面连接')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("target.jpg")
