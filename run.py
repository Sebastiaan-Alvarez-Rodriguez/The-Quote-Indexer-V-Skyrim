import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from src.quotes.manager import QuoteManager
from src.stt.stt import QuoteSpeech

import src.general.general as g

g.abs_loc = os.path.abspath(os.path.dirname(__file__))

quotespeech = QuoteSpeech('models/')
quotemanager= QuoteManager()


class App(QWidget):
    # https://pythonspot.com/pyqt5-buttons/
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 1200
        self.height = 800
        self.setWindowTitle('The Quote Indexer - V: Skyrim')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.speechButton()
        self.centralize()

    def speechButton(self):
        self.speech_button = QtWidgets.QPushButton(self)
        self.speech_button.setObjectName("speech_button")
        self.speech_button.setGeometry(QtCore.QRect(20, 20, 512, 512))
        # self.speech_button.setStyleSheet("speech_button{background: transparent;background-color: rgba(255, 255, 255, 0); border: 0px;}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/res/mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speech_button.setIcon(icon)
        self.speech_button.setIconSize(QtCore.QSize(512, 512))
        self.speech_button.clicked.connect(self.receive_quote)

    def centralize(self):
        fg = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    @pyqtSlot()
    def receive_quote(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/res/mic_active.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speech_button.setIcon(icon)

        # detected = quotespeech.get_speech()
        import time
        time.sleep(1)


# https://build-system.fman.io/pyqt5-tutorial

#Tutorial
# https://www.learnpyqt.com/
#UI Material theme
# https://github.com/Alexhuszagh/BreezeStyleSheets

def main():
    sys_argv = sys.argv
    # sys_argv += ['--style', 'Fusion']
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

    # loc = 'dataset/out_compressed.tsv'
    # x = SkyQuoteList(loc)
    # print('Read complete')
    # item = x.find('Not stand by dragon slaughters people')
    # if item != None:
    #     print(f'Found: {item}')
    # else:
    #     print('Did not find anything significant (>0.3)')

if __name__ == '__main__':
    main()