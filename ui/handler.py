import sys
import os
import threading
import webbrowser
from playsound import playsound

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
import qdarkstyle

from ui.ui import App

from src.quotes.manager import QuoteManager
from src.stt.stt import QuoteSpeech
import src.general.general as g

'''Main handler for this program. Setups all UI interaction callbacks'''
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
        self.enable_speech()

        self.current_quote = None

    # Go to main QT loop
    def run(self):
        self.app.show()
        sys.exit(self.qapp.exec_())

    # Disable speech button
    def disable_speech(self):
        self.app.speech_button.setEnabled(False)
    # Enable speech button
    def enable_speech(self):
        self.app.speech_button.setEnabled(True)

    # Disable url button
    def disable_url(self):
        self.app.url_button.setEnabled(False)
    # Enable url button
    def enable_url(self):
        self.app.url_button.setEnabled(True)

    # Disable speaker button
    def disable_speaker(self):
        self.app.speaker_button.setEnabled(False)
    # Enable url button
    def enable_speaker(self):
        self.app.speaker_button.setEnabled(True)

    # Callback for list selection changes
    def on_list_selected_changed(self, cur, prev):
        self.quotemanager.switch_context(self.app.model.item(cur.row()).text())
    
    # Callback for speech button clicks
    def on_speech_button_clicked(self):
        print('Received request for quote input')
        x = threading.Thread(target=self.process_quote).start()
        self.disable_speech()

    # Callback for speech button clicks
    def on_url_button_clicked(self):
        if self.current_quote != None:
            url = self.current_quote.get_url()
            if url != None:
                webbrowser.open(url)

    # Callback for speaker button clicks (we play sound here)
    def on_speaker_button_clicked(self):
        if self.current_quote != None:
            path = self.current_quote.get_audio_path()
            if path != None:
                playsound(path)

    # Main quote handler: On click, activates mic, gets quote to text, searches loaded dataset for matches,
    # displays match if it exists, enables speaker button and url button if applicable
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

            audio_file = quote.get_audio_path(os.path.join(g.snd_loc,self.quotemanager.get_current_context()))
            if audio_file != None and os.path.isfile(audio_file):
                self.enable_speaker()
            else:
                self.disable_speaker()
            
            extra_info = quote.get_extra_info()
            if extra_info != None:
                self.app.set_extra_text(extra_info)
            else:
                self.app.set_extra_text('No extra information available')
        self.enable_speech()
