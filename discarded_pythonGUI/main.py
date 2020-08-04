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
        # 创建按钮实例
        self.causeDamage_button = QPushButton(self)
        self.resetLP_button = QPushButton(self)
        self.rollDice_button = QPushButton(self)
        self.rollCoin_button = QPushButton(self)
        self.init_buttons()

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

    def init_buttons(self):
        self.causeDamage_button.setText("造成伤害")
        self.resetLP_button.setText("重设LP")
        self.rollDice_button.setText("掷d6")
        self.rollCoin_button.setText("投硬币")

        self.causeDamage_button.setStyleSheet("QPushButton{color:black}"
                                              "QPushButton{background-color:white}"
                                              "QPushButton{border:2px}"
                                              "QPushButton{padding:20px 40px}"
                                              "QPushButton{font-size: 48px}"
                                              "QPushButton{font-family:'Microsoft YaHei'}")
        self.resetLP_button.setStyleSheet("QPushButton{color:black}"
                                          "QPushButton{background-color:white}"
                                          "QPushButton{border:2px}"
                                          "QPushButton{padding:20px 40px}"
                                          "QPushButton{font-size: 48px}"
                                          "QPushButton{font-family:'Microsoft YaHei'}")
        self.rollDice_button.setStyleSheet("QPushButton{color:black}"
                                           "QPushButton{background-color:white}"
                                           "QPushButton{border:2px}"
                                           "QPushButton{padding:20px 40px}"
                                           "QPushButton{font-size: 48px}"
                                           "QPushButton{font-family:'Microsoft YaHei'}")
        self.rollCoin_button.setStyleSheet("QPushButton{color:black}"
                                           "QPushButton{background-color:white}"
                                           "QPushButton{border:2px}"
                                           "QPushButton{padding:20px 40px}"
                                           "QPushButton{font-size: 48px}"
                                           "QPushButton{font-family:'Microsoft YaHei'}")

        self.causeDamage_button.setGeometry(80, 230, 280, 100)
        self.resetLP_button.setGeometry(80, 380, 280, 100)
        self.rollDice_button.setGeometry(80, 530, 280, 100)
        self.rollCoin_button.setGeometry(80, 680, 280, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()
    sys.exit()
