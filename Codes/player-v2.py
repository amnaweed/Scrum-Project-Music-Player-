# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player-interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class Ui_MainWindow(QWidget):

##    def __init__(self):
##        self.setAcceptDrops(True)

    #create media player object
    mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
    repeatMedia = False
    repeatItem = ""


    def formatTime(self, ms):
        
        h, r = divmod(ms, 3600000)
        m, r = divmod(r, 60000)
        s, _ = divmod(r, 1000)
        return ("%02d:%02d:%02d" % (h,m,s)) if h else ("%02d:%02d" % (m,s))

    def browseFile(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.play()
        elif self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.mediaPlayer.play()
        else:
            media, _ = QFileDialog.getOpenFileName(self, "Open Video")

            if media != "":     
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(media)))
                self.mediaPlayer.play()

    def openFile(self):
        media, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if media != "":     
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(media)))
            self.mediaPlayer.play()
        
    def pauseVideo(self):
        self.mediaPlayer.pause()

    def stopVideo(self):
        self.mediaPlayer.stop()
        
    def vidPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def locationChanged(self, position):
        self.duration.setValue(position)

        if position >= 0:
            self.startTime.setText(self.formatTime(position))

        if self.mediaPlayer.state() == 0:
            
            if self.repeatMedia:
                self.mediaPlayer.play()
            else:
##                self.duration.setRange(0,0)
                self.startTime.setText("--:--")
                self.endTime.setText("--:--")

    def durationChanged(self, duration):
        self.duration.setRange(0, duration)

        playTime = self.mediaPlayer.duration()
        self.endTime.setText(self.formatTime(playTime))

    def volumeControl(self, percentage):
        self.mediaPlayer.setVolume(percentage)

    def loopMedia(self):
        self.repeatMedia = True

##    def dragEnterEvent(self, e):
##        if e.mimeData().hasUrls():
##            e.acceptProposedAction()
##
##    def dropEvent(self, e):
##        for url in e.mimeData().urls():
##            media = url
##
##        print(media)
##        self.model.layoutChanged.emit()
##
##        # If not playing, seeking to first of newly added + play.
##        if self.player.state() != QMediaPlayer.PlayingState:
##            i = self.playlist.mediaCount() - len(e.mimeData().urls())
##            self.playlist.setCurrentIndex(i)
##            self.player.play()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgba(3,146,251,0.8);\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #E5F1FB;\n"
"}\n"
"\n"
"#translation {\n"
"    font-size: 40px;\n"
"    color: #E5F1FB;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #E5F1FB;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-size: 40px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: #333;\n"
"    background: #fff;\n"
"    border-radius: 8px;\n"
"    font-size: 17px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:focus{\n"
"    background: rgba(255, 255, 255, 0.8);\n"
"    color: #000;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.videoWidget = QVideoWidget(self.centralwidget)
        self.videoWidget.setGeometry(QtCore.QRect(0, 0, 700, 391))
        self.videoWidget.setMinimumSize(QtCore.QSize(700, 200))
        self.videoWidget.setObjectName("videoWidget")

        ################### Video Widget ################
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        #################################################
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 390, 691, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startTime = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.startTime.setObjectName("startTime")
        self.horizontalLayout.addWidget(self.startTime)
        self.duration = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.duration.setOrientation(QtCore.Qt.Horizontal)
        self.duration.setObjectName("duration")
        self.horizontalLayout.addWidget(self.duration)

        ################### Video Slider #################
        self.duration.setRange(0,0)
        self.duration.sliderMoved.connect(self.vidPosition)
        self.mediaPlayer.positionChanged.connect(self.locationChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        ##################################################
        
        self.endTime = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.endTime.setObjectName("endTime")
        self.horizontalLayout.addWidget(self.endTime)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.play = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.play.setObjectName("play")
        self.horizontalLayout_3.addWidget(self.play)

        ################### Play Button ##################
        self.play.clicked.connect(self.browseFile)
        ##################################################
        
        self.pause = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pause.setObjectName("pause")
        self.horizontalLayout_3.addWidget(self.pause)

        ################### Pause Button #################
        self.pause.clicked.connect(self.pauseVideo)
        ##################################################
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.prev = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.prev.setObjectName("prev")
        self.horizontalLayout_3.addWidget(self.prev)
        self.stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop.setObjectName("stop")
        self.horizontalLayout_3.addWidget(self.stop)

        ################### Stop Button ##################
        self.stop.clicked.connect(self.stopVideo)
        ##################################################
        
        self.next = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.next.setObjectName("next")
        self.horizontalLayout_3.addWidget(self.next)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.repeat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.repeat.setEnabled(True)
        self.repeat.setStatusTip("")
        self.repeat.setObjectName("repeat")
        self.horizontalLayout_3.addWidget(self.repeat)

        ################### Repeat Button ################
        self.repeat.clicked.connect(self.loopMedia)
        ##################################################

        
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.volume = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.volume.setOrientation(QtCore.Qt.Vertical)
        self.volume.setObjectName("volume")
        self.horizontalLayout_3.addWidget(self.volume)

        ################### Volume Slider ################
        self.volume.setRange(0,100)
        self.volume.setValue(100)
        self.volume.valueChanged.connect(self.volumeControl)
        ##################################################
        
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionPlaylist = QtWidgets.QAction(MainWindow)
        self.actionPlaylist.setObjectName("actionPlaylist")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionPlaylist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        ################### Open Button ##################
        self.actionOpen.triggered.connect(self.openFile)
        ##################################################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startTime.setText(_translate("MainWindow", "--:--"))
        self.endTime.setText(_translate("MainWindow", "--:--"))
        self.play.setText(_translate("MainWindow", "play"))
        self.pause.setText(_translate("MainWindow", "pause"))
        self.prev.setText(_translate("MainWindow", "Previous"))
        self.stop.setText(_translate("MainWindow", "stop"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.repeat.setText(_translate("MainWindow", "Repeat"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionPlaylist.setText(_translate("MainWindow", "Playlist"))
        self.actionClose.setText(_translate("MainWindow", "Quit"))
        self.actionOpen.setText(_translate("MainWindow", "Open File..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
