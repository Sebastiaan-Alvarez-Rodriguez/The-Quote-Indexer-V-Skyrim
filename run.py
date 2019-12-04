import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


from ui.handler import UIHandler

import src.general.general as g

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

def main():
    g.abs_loc = os.path.abspath(os.path.dirname(__file__))
    g.dyn_loc = os.path.join(g.abs_loc, 'dynamic')
    g.cnf_loc = os.path.join(g.abs_loc, 'configs')

    handler = UIHandler()
    handler.run()

if __name__ == '__main__':
    main()