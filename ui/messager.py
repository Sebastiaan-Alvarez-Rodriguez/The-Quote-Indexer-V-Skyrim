from PyQt5.QtWidgets import QMessageBox
from enum import Enum

class Severity(Enum):
    QUESTION = 0
    INFORMATION = 1
    WARNING = 2
    CRITICAL = 3

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

def msg(text, title='The Quote Indexer - V: Skyrim', severity=Severity.WARNING):
    __msg(text, title, severity).exec_()

# buttons: QMessageBox.Ok, Open, ...Save, Cancel, Close, Yes, No, Abort, Retry, Ignore
def msg_ignore_cancel(text, fun, title='The Quote Indexer - V: Skyrim', severity=Severity.WARNING):
    m = __msg(text, title, severity)
    m.setStandardButtons(QMessageBox.Ignore | QMessageBox.Cancel)
    m.buttonClicked.connect(fun) #def fun(x): print(x.text)...  text of button will be printed
    m.exec_()