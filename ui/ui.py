import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

import src.general.general as g

def make_speech_button(parent):
    speech_button = QtWidgets.QPushButton(parent)
    speech_button.setObjectName('speech_button')
    speech_button.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(os.path.join(g.abs_loc,'ui','res','mic.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    speech_button.setIcon(icon)
    speech_button.setIconSize(QtCore.QSize(244, 128))
    speech_button.setEnabled(False)
    return speech_button

def make_url_button(parent):
    url_button = QtWidgets.QPushButton(parent)
    url_button.setObjectName('url_button')
    url_button.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(os.path.join(g.abs_loc,'ui','res','chain_link.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    url_button.setIcon(icon)
    url_button.setIconSize(QtCore.QSize(128, 128))
    url_button.setEnabled(False)
    return url_button

def make_speaker_button(parent):
    speaker_button = QtWidgets.QPushButton(parent)
    speaker_button.setObjectName('speaker_button')
    speaker_button.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(os.path.join(g.abs_loc, 'ui','res','speaker.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    speaker_button.setIcon(icon)
    speaker_button.setIconSize(QtCore.QSize(128, 128))
    speaker_button.setEnabled(False)
    return speaker_button

def make_help_field(parent):
    help_text = QtWidgets.QLabel(parent)
    help_text.setObjectName('help_text')
    help_text.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
    help_text.setFont(QtGui.QFont('Times', 28, QtGui.QFont.Bold))
    help_text.setText('Press speaker button and start speaking...')
    return help_text

def make_quote_field(parent):
    quote_text = QtWidgets.QLabel(parent)
    quote_text.setObjectName('quote_text')
    quote_text.setFont(QtGui.QFont('Times', 24, QtGui.QFont.Bold))
    quote_text.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))
    quote_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
    quote_text.setText('"Quotes will appear here"\n- Sebastiaan')
    quote_text.setWordWrap(True)
    return quote_text

def make_moreinfo_field(self):
    more_info = QtWidgets.QLabel(self)
    more_info.setObjectName('more_info')
    more_info.setFont(QtGui.QFont('Times', 20, QtGui.QFont.Bold))
    more_info.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))
    more_info.setText('Extra info will appear here')
    more_info.setWordWrap(True)
    return more_info

def make_listview(self):
    list_view = QtWidgets.QListView(self)
    list_view.setGeometry(QtCore.QRect(20, 256, 256, 256))
    list_view.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding))
    list_view.setObjectName('listView')
    return list_view

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.width = 1200
        self.height = 800
        self.setWindowTitle('The Quote Indexer - V: Skyrim')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        self.speech_button = make_speech_button(self)
        self.url_button    = make_url_button(self)
        self.speaker_button= make_speaker_button(self)
        self.help_text     = make_help_field(self)
        self.quote_text    = make_quote_field(self)
        self.more_info     = make_moreinfo_field(self)
        self.list_view     = make_listview(self)
        self.make_layout()
        self.centralize()

    def make_layout(self):
        layout = QtWidgets.QGridLayout(self)
        layout.setObjectName('layout_out')
        layout.setGeometry(QtCore.QRect(self.left, self.top, self.width, self.height))
        layout.addWidget(self.speech_button,  0,0)
        layout.addWidget(self.help_text,      0,1,1,10)
        layout.addWidget(self.list_view,      1,0,10,1)
        layout.addWidget(self.quote_text,     1,1,7,10)
        layout.addWidget(self.more_info,      7,1,2,10)
        layout.addWidget(self.url_button,    10,1, QtCore.Qt.AlignCenter)
        layout.addWidget(self.speaker_button,10,2, QtCore.Qt.AlignCenter)

    def centralize(self):
        fg = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    def populate_list(self, items):
        self.model = QtGui.QStandardItemModel(self.list_view)

        for x in items:
            item = QtGui.QStandardItem(x)
            item.setEditable(False)
            self.model.appendRow(item)
        self.list_view.setModel(self.model)
        self.list_view.setSelectionMode(QtWidgets.QListView.SingleSelection)

    def select_first_item(self):
        self.list_view.selectionModel().select(self.model.index(0,0), self.list_view.selectionModel().Select)
        self.on_listview_selected_changed(self.model.index(0,0), None)

    def set_help_text(self, text):
        self.help_text.setText(text)

    def set_quote_text(self, text):
        self.quote_text.setText(text)

    def set_extra_text(self, text):
        self.more_info.setText(text)

    def set_list_selected_changed_listener(self, fun):
        self.list_view.selectionModel().currentChanged.connect(fun)

    def set_speech_button_clicked_listener(self, fun):
        self.speech_button.clicked.connect(fun)

    def set_url_button_clicked_listener(self, fun):
        self.url_button.clicked.connect(fun)

    def set_speaker_button_clicked_listener(self, fun):
        self.speaker_button.clicked.connect(fun)