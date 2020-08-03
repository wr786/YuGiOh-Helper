# -*- coding: utf-8 -*-
# author: wr786
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_window()
        self.show()

    def init_window(self):
        self.setWindowTitle('YuGiOh! Helper © wr786')
        self.setWindowIcon(QIcon('.\\resource\\ICON.ico'))
        # self.setWindowFlags(Qt.FramelessWindowHint) # 隐藏边框
        self.setFixedSize(1600, 1080)
        # 居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # 背景
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('.\\resource\\bg.jpg')))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()
    sys.exit()