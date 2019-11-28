import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


from src.quotes.quotelist import SkyQuoteList

# convert: pyuic5 ui/src/main.ui -o ui/win_main.py

from src.stt.stt import QuoteSpeech

# quotespeech = QuoteSpeech('models/')

# Maybe program QT shit myself: https://pythonspot.com/pyqt5-buttons/
# https://build-system.fman.io/pyqt5-tutorial
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        self.centralize()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.clicked.connect(self.on_click)
        self.show()

    def centralize(self):
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

#Tutorial
# https://www.learnpyqt.com/
#UI Material theme
#https://doc.qt.io/qt-5/qtquickcontrols2-material.html

def main():
    sys_argv = sys.argv
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    # sys_argv += ['--style', 'Fusion']
    # app = QtWidgets.QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # app.exec()
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