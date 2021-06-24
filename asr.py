import os
import time

from PyQt5 import QtWidgets, QtGui, QtCore, uic
import threading
import asrInterface
import sys
# import recorder
import wave
import numpy as np
import speech_recognition as sr
import baiduapi.asr_json as baidu_api


class Controller:
    def play_music(self):
        if sys.platform == 'darwin':
            os.system('open ' + 'music.mp3')
        # elif sys.platform[:3] == 'win':
        #     win32api.ShellExecute(0, 'open', 'E:\\song.wma', '', '', 1)



    def open_text(self):
        if sys.platform == 'darwin':
            os.system('open ' + 'test.txt')

    def open_img(self):
        if sys.platform == 'darwin':
            os.system('open ' + 'test.jpg')

    def play_video(self):
        if sys.platform == 'darwin':
            os.system('open ' + 'video.MP4')
c = Controller()
def get_speech_from_mic(r, mic):
    # getting wav file from mic
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('start')

        try:
            audio = r.listen(source, timeout=5)
            wav_data = audio.get_wav_data()
            wf = wave.open('tmp.wav', 'wb')  # type: wave
            wf.setnchannels(1)

            wf.setsampwidth(2)
            wf.setframerate(8000)
            wf.writeframes(np.array(wav_data).tostring())
            wf.close()
            get_text_from_api()
            application.ui.update_label_6('点击按钮来和我对话。')
        except:
            application.ui.update_label_6('没有听清，您可以再说一次吗？')



def get_text_from_api():

    try:
        print('start')
        j = baidu_api.get_json()
        application.ui.update_label_5(j['result'][0])
        keyword = j['result'][0]
        if keyword[:2] == '播放':
            c.play_music()
        elif keyword[:4] == '打开文档':
            c.open_text()
        elif keyword[:2] == '看图':
            c.open_img()

        elif keyword[:3] == '看视频':
            c.play_video()
    except:
        application.ui.update_label_5('Something wrong happens.')


class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = asrInterface.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.retranslateUi(self)


def onclicked():
    speech_interaction()

t = threading.Thread()

def update_dots():
    i = 0
    while True:
        if not t.is_alive():
            return
        application.ui.update_label_5('..' * i)
        i += 1
        time.sleep(1)

def speech_interaction():
    global t
    if t.is_alive():

        return

    print(threading.current_thread())
    r = sr.Recognizer()
    try:
        mic = sr.Microphone()
        t = threading.Thread(target=get_speech_from_mic, args=[r, mic])
        t.start()
        application.ui.update_label_6('你说，我在听')
        # t.join()
        i = 0
        t2 = threading.Thread(target=update_dots)
        t2.start()

    except:
        application.ui.update_label_6('请检查麦克风是否工作')


app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())

