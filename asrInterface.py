# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QIcon
from PyQt5 import Qt

class MyQLabel(QtWidgets.QLabel):
    # make the gif clickable
    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.voiceFig = MyQLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(70, 50, 161, 121))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")
        import asr
        self.voiceFig.connect_customized_slot(asr.speech_interaction)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 220, 201, 150))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")



        # status label created to show the current status
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ffffff;")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QtCore.QRect(60, 380, 201, 200))
        self.label_5.setAlignment(QtCore.Qt.AlignTop)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 160, 201, 51))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #948d8d;")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def update_label_5(self, text):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", text))

    def update_label_6(self, text):
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("MainWindow", text))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_4.setText(_translate("MainWindow", "你好，这是一个中文语音助手。\n\n你可以这样问我：\n1. 说\"播放\"以播放音乐\n" + "2. 说\"打开文档\"以查看记事本文档\n" +
                                                      "3. 说\"看图\"以查看示例图片\n" +
                                                        "4. 说\"看视频\"以查看抖音小视频\n"))
        # self.label_5.setText(_translate("MainWindow", "I\'m hearing..."))
        self.label_6.setText(_translate("MainWindow", "点击按钮来和我对话。"))
    # def onclicked(self):
    #     # self.voiceFig.movie().setPaused(True)
    #     # print('abc')
    #     asr.speech_interaction()