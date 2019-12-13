from PyQt5.QtWidgets import QMessageBox
from enum import Enum

'''Enum to indicate message severity'''
class Severity(Enum):
    QUESTION = 0
    INFORMATION = 1
    WARNING = 2
    CRITICAL = 3

# Internal function, do not call from outside of this file. Builds and returns a message object
def __msg(text, title, severity):
    x = QMessageBox()
    x.setWindowTitle(title)
    x.setText(text)

    if severity == Severity.QUESTION:
        x.setIcon(QMessageBox.Question)
    elif severity == Severity.INFORMATION:
        x.setIcon(QMessageBox.Information)
    elif severity == Severity.WARNING:
        x.setIcon(QMessageBox.Warning)
    elif severity == Severity.CRITICAL:
        x.setIcon(QMessageBox.Critical)
    return x

# Constructs and displays a message, with an OK button
def msg(text, title='The Quote Indexer - V: Skyrim', severity=Severity.WARNING):
    __msg(text, title, severity).exec_()

# Constructs and displays a message with an ignore and cancel button
# Callback can differentiate between which button was clicked by checking whether button.text().lower() is 'ignore' or 'cancel'
def msg_ignore_cancel(text, fun, title='The Quote Indexer - V: Skyrim', severity=Severity.WARNING):
    m = __msg(text, title, severity)
    m.setStandardButtons(QMessageBox.Ignore | QMessageBox.Cancel)
    m.buttonClicked.connect(fun)
    m.exec_()