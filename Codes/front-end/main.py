import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# SPLASH SCREEN
from splash import Ui_SplashScreen

# MAIN WINDOW
from player import Ui_MainWindow

# GLOBALS
counter = 0

# Application Main Page
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.images()




    def images (self):
        QtCore.QTimer.singleShot(5000, lambda: self.ui.graphicsView.setStyleSheet(
            "background-image: url(:/imgs/photo-1508951598074-bcc78111198c.jpg)"))
        QtCore.QTimer.singleShot(10000, lambda: self.ui.graphicsView.setStyleSheet(
            "background-image: url(:/imgs/13312.jpg)"))
        QtCore.QTimer.singleShot(15000, lambda: self.ui.graphicsView.setStyleSheet(
            "background-image: url(:/imgs/photo-1517928260182-5688aead3066.jpg)"))
        QtCore.QTimer.singleShot(20000, lambda: self.ui.graphicsView.setStyleSheet(
            "background-image: url(:/imgs/photo-1529963183134-61a90db47eaf.jpg)"))
        QtCore.QTimer.singleShot(25000, lambda: self.ui.graphicsView.setStyleSheet(
            "background-image: url(:/imgs/sky-828648_1280.jpg)"))
        QtCore.QTimer.singleShot(30000, lambda: self.ui.graphicsView.setStyleSheet(
            "background-image: url(:/imgs/photo-1516450360452-9312f5e86fc7.jpg)"))








# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # UI  INTERFACE CODES

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # Q TIMER START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(30)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO THE SYSTEM <strong>♪</strong>")

        # Change Texts
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>Please wait...</strong>"))



        # SHOW MAIN WINDOW
        self.show()
        # END

    # Progress bar function
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
