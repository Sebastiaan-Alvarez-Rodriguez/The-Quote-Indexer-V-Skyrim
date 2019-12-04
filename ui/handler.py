import sys
import threading
import webbrowser

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from ui.ui import App

from src.quotes.manager import QuoteManager
from src.stt.stt import QuoteSpeech

class UIHandler(object):
    """docstring for UIHandler"""
    def __init__(self):
        super(UIHandler, self).__init__()
        self.qapp = QApplication(sys.argv)
        self.quotespeech = QuoteSpeech('models/')
        self.quotemanager= QuoteManager()
        self.app = App()
        self.app.populate_list(self.quotemanager.get_contexts())
        self.app.set_list_selected_changed_listener(self.on_list_selected_changed)
        self.app.set_speech_button_clicked_listener(self.on_speech_button_clicked)
        self.app.set_url_button_clicked_listener(self.on_url_button_clicked)
        self.finish_speech()

        self.current_quote = None

    def run(self):
        self.app.show()
        sys.exit(self.qapp.exec_())

    def start_speech(self):
        self.app.speech_button.setEnabled(False)

    def finish_speech(self):
        self.app.speech_button.setEnabled(True)

    def disable_url(self):
        self.app.url_button.setEnabled(False)

    def enable_url(self):
        self.app.url_button.setEnabled(True)

    def on_list_selected_changed(self, cur, prev):
        print(f'You clicked on item with text: {self.app.model.item(cur.row()).text()}')
        self.quotemanager.switch_context(self.app.model.item(cur.row()).text())
        #TODO: make sure that an item looks less ugly, and has a big icon on the side (at least 24x24)
    
    def on_speech_button_clicked(self):
        print('Received request for quote input')
        x = threading.Thread(target=self.process_quote).start()
        self.start_speech()

    def on_url_button_clicked(self):
        if self.current_quote != None:
            url = self.current_quote.get_url()
            if url != None:
                webbrowser.open(url)

    def process_quote(self):
        quote = ''
        while quote == '':
            self.app.set_help_text('Listening...')
            quote = self.quotespeech.get_speech()
            print(f'Speech recognized: {quote}')
        self.app.set_help_text('Finding quote...')
        quote = self.quotemanager.find(quote)
        print(f'Matching quote: {quote}')
        if quote == None:
            self.app.set_help_text("Sorry, didn't catch that. Please try again!")
            self.disable_url()
        else:
            self.current_quote = quote
            self.app.set_help_text("Found something!")
            self.app.set_quote_text(quote.get_quote())
            self.enable_url()
            
        self.finish_speech()
