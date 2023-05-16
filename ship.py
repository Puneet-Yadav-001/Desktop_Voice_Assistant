from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer, QTime
from shipUi import Ui_MainWindow
import sys
import Main

class MainThread(QThread):
    def __int__(self):
        super(MainThread,self).__int__()

    def run(self):
        self.start_Gui()

    def start_Gui(self):
        Main.greet()
        Main.ai_tasks()

startvar = MainThread()

class Ui_start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.shipui = Ui_MainWindow()

        self.shipui.setupUi(self)
         #triggering action when my button gets clicked
        self.shipui.startButton.clicked.connect(self.startFunc)

        self.shipui.exitButton.clicked.connect(self.close)

    def startFunc(self):    #function to move my gif files
        self.shipui.movies = QtGui.QMovie("intro.gif")
        self.shipui.gif.setMovie(self.shipui.movies)
        self.shipui.movies.start()


        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startvar.start()

    def showtime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString("hh:mm:ss")
        self.shipui.timebox.setText(label_time)

Ui_App = QApplication(sys.argv)
uiship = Ui_start()  #starting the ui class obj
uiship.show()
exit(Ui_App.exec_())