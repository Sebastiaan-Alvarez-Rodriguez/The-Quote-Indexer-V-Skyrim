import sys
import threading
import webbrowser
from playsound import playsound

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
import qdarkstyle

from ui.ui import App

from src.quotes.manager import QuoteManager
from src.stt.stt import QuoteSpeech

class UIHandler(object):
    def __init__(self):
        super(UIHandler, self).__init__()
        self.qapp = QApplication(sys.argv)
        self.quotespeech = QuoteSpeech()
        self.quotemanager= QuoteManager()
        self.app = App()
        self.app.populate_list(self.quotemanager.get_contexts())
        self.app.set_list_selected_changed_listener(self.on_list_selected_changed)
        self.app.set_speech_button_clicked_listener(self.on_speech_button_clicked)
        self.app.set_url_button_clicked_listener(self.on_url_button_clicked)
        self.app.set_speaker_button_clicked_listener(self.on_speaker_button_clicked)
        self.qapp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
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

    def disable_speaker(self):
        self.app.speaker_button.setEnabled(False)

    def enable_speaker(self):
        self.app.speaker_button.setEnabled(True)

    def on_list_selected_changed(self, cur, prev):
        self.quotemanager.switch_context(self.app.model.item(cur.row()).text())
    
    def on_speech_button_clicked(self):
        print('Received request for quote input')
        x = threading.Thread(target=self.process_quote).start()
        self.start_speech()

    def on_url_button_clicked(self):
        if self.current_quote != None:
            url = self.current_quote.get_url()
            if url != None:
                webbrowser.open(url)

    def on_speaker_button_clicked(self):
        if self.current_quote != None:
            path = self.current_quote.get_audio_path()
            if path != None:
                playsound(path)

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
        else:
            self.current_quote = quote
            self.app.set_help_text('Found something!')
            self.app.set_quote_text(quote.get_quote())
            if self.current_quote.get_url() != None:
                self.enable_url()
            else:
                self.disable_url()

            if quote.get_audio_path() != None:
                self.enable_speaker()
            else:
                self.disable_speaker()
            
            extra_info = quote.get_extra_info()
            if extra_info != None:
                self.app.set_extra_text(extra_info)
            else:
                self.app.set_extra_text('No extra information available')
        self.finish_speech()
