import sys
import os
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from src.quotes.manager import QuoteManager
from src.stt.stt import QuoteSpeech

import src.general.general as g

class App(QWidget):
    # https://pythonspot.com/pyqt5-buttons/
    def __init__(self):
        super().__init__()
        self.quotespeech = QuoteSpeech('models/')
        self.quotemanager= QuoteManager()

        self.left = 0
        self.top = 0
        self.width = 1200
        self.height = 800
        self.setWindowTitle('The Quote Indexer - V: Skyrim')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        self.speechButton()
        self.helpField()
        self.quoteField()
        self.listView()
        self.layoutMake()
        self.populateListView()
        self.centralize()

    def layoutMake(self):
        layout = QtWidgets.QGridLayout(self)
        layout.setObjectName("layout_out")
        layout.setGeometry(QtCore.QRect(self.left, self.top, self.width, self.height))
        # layout_out.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        layout.addWidget(self.speech_button, 0,0)
        layout.addWidget(self.help_text, 0,1,1,10)
        layout.addWidget(self.list_view, 1,0)
        layout.addWidget(self.quote_text, 1,1)

    def speechButton(self):
        self.speech_button = QtWidgets.QPushButton(self)
        self.speech_button.setObjectName("speech_button")
        self.speech_button.setGeometry(QtCore.QRect(20, 20, 256, 128))
        self.speech_button.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        # self.speech_button.setStyleSheet("speech_button{background: transparent;background-color: rgba(255, 255, 255, 0); border: 0px;}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/res/mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speech_button.setIcon(icon)
        self.speech_button.setIconSize(QtCore.QSize(244, 128))
        self.speech_button.clicked.connect(self.receive_quote)

    def helpField(self):
        self.help_text = QtWidgets.QLabel(self)
        self.help_text.setObjectName("help_text")
        self.help_text.setGeometry(QtCore.QRect(20, 20, self.width-256-20, 128))
        self.help_text.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        self.help_text.setFont(QtGui.QFont("Times", 28, QtGui.QFont.Bold))
        self.help_text.setText('Press speaker button and start speaking...')

    def quoteField(self):
        self.quote_text = QtWidgets.QLabel(self)
        self.quote_text.setObjectName("quote_text")
        self.quote_text.setGeometry(QtCore.QRect(20, 20+128, self.width-256-20, self.height-20-128))
        self.quote_text.setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))
        self.quote_text.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))
        self.quote_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.quote_text.setText('"Quotes will appear here"\n- Sebastiaan')
        self.quote_text.setWordWrap(True)

    def listView(self):
        self.list_view = QtWidgets.QListView(self)
        self.list_view.setGeometry(QtCore.QRect(20, 256, 256, 256))
        self.list_view.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding))
        self.list_view.setObjectName("listView")

    def centralize(self):
        fg = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    def populateListView(self):
        self.model = QtGui.QStandardItemModel(self.list_view)

        for x in self.quotemanager.get_contexts():
            print('context: '+str(x))
            item = QtGui.QStandardItem(x)
            self.model.appendRow(item)
        # item = QtGui.QStandardItem('oooooooof what a very most super ultra long text window story option to select')

        self.list_view.setModel(self.model)
        self.list_view.setSelectionMode(QtWidgets.QListView.SingleSelection)
        self.list_view.selectionModel().currentChanged.connect(self.on_listview_selected_changed)
        self.list_view.selectionModel().select(self.model.index(0,0), self.list_view.selectionModel().Select)
        self.on_listview_selected_changed(self.model.index(0,0), None)

    def on_listview_selected_changed(self, cur, prev):
        print(f'You clicked on item with text: {self.model.item(cur.row()).text()}')

    @pyqtSlot()
    def receive_quote(self):
        print('Received request for quote input')
        x = threading.Thread(target=self.process_quote).start()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/res/mic_active.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speech_button.setIcon(icon)
        self.speech_button.clicked.disconnect()

    def process_quote(self):
        quote = ''
        while quote == '':
            quote = self.quotespeech.get_speech()
            print(f'Speech recognized: {quote}')
        quote = self.quotemanager.find(quote)
        print(f'Matching quote: {quote}')
        if quote == None:
            self.quote_text.setText("Sorry, didn't catch that")
        else:
            self.quote_text.setText(str(quote))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/res/mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speech_button.setIcon(icon)
        self.speech_button.clicked.connect(self.receive_quote)


# https://build-system.fman.io/pyqt5-tutorial

#Tutorial
# https://www.learnpyqt.com/
#UI Material theme
# https://github.com/Alexhuszagh/BreezeStyleSheets

#Okay working quotes: Luid spreken, linker middelvinger afstand tot mic, mic gericht op neus, mic in gat voor oortjes
# Skyrim
# "So you are interested in my potions and ingredients?"...
# "Looking to protect yourself, or deal some damage?"
# "By the nine"
# "I'll be the one asking the questions"
# "Has wares, if you have coin" (or even: "Khajit has wares, if you have coin")
# "M'aiq knows many things, no?"
# "Another new apprentice, I see"
# "In time, I believe he will be more trusting"
# "Get on with it"
# "I believe I made myself rather clear"
# "We have company"
# "These vampires are becoming a real menace"
# "Got to thinking, maybe I am the dragonborn and just don't know it yet"
# "Guard migh get nervous, a man approaches with his weapns drawn"
# "I used to be an adventurer like you, but then I took an arrow in the knee"
# "Come to Dragonsreach to discuss the war, like the rest of the great warriors?"
# "What is better? To be born good, or to overcome evil?" (poorish)
# "the first thing to understand is that magic is, by its very nature very dangerous"
# "I would suggest you do not spread this rumor further" (poorish)
# "So I can stab you in the back" (poor)

# Other
# "To be or not to be, that is the question"

def fill_globals():
    g.abs_loc = os.path.abspath(os.path.dirname(__file__))
    g.dyn_loc = os.path.join(g.abs_loc, 'dynamic')

def main():
    fill_globals()
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