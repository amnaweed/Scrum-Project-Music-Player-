# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QIcon

class Ui_MainWindow(QWidget):

    #create media player object
    mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
    repeatMedia = False
    repeatItem = ""
    playlist = QMediaPlaylist()


    def formatTime(self, ms):
        
        h, r = divmod(ms, 3600000)
        m, r = divmod(r, 60000)
        s, _ = divmod(r, 1000)
        return ("%02d:%02d:%02d" % (h,m,s)) if h else ("%02d:%02d" % (m,s))

    def browseFile(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.play.setIcon(self.playIcon)
            self.mediaPlayer.pause()
        elif self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.play.setIcon(self.pauseIcon)
            self.mediaPlayer.play()
        elif not(self.playlist.isEmpty()):
            self.mediaPlayer.setPlaylist(self.playlist)
            self.mediaPlayer.play()
            self.play.setIcon(self.pauseIcon)
        else:
            media, _ = QFileDialog.getOpenFileName(self, "Open Video")

            if media != "":     
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(media)))
                self.playlist.addMedia(
                    QMediaContent(
                        QUrl.fromLocalFile(media)
                    )
                )
                self.mediaPlayer.play()
                self.play.setIcon(self.pauseIcon)

    def openFile(self):
        media, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if media != "":     
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(media)))
            self.mediaPlayer.play()

    def closeFile(self):
        quit()
        
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
                self.duration.setValue(0)
                self.play.setIcon(self.playIcon)
                self.startTime.setText("--:--")
                self.endTime.setText("--:--")

    def durationChanged(self, duration):
        self.duration.setRange(0, duration)

        playTime = self.mediaPlayer.duration()
        self.endTime.setText(self.formatTime(playTime))

    def volumeControl(self, percentage):
        self.mediaPlayer.setVolume(percentage)

        if percentage <= 100 and percentage >= 60:
            self.volume.setIcon(self.volumeUp)
        elif percentage < 60 and percentage >= 30:
            self.volume.setIcon(self.volumeMed)
        elif percentage < 30 and percentage >= 1:
            self.volume.setIcon(self.volumeDown)
        else:
            self.volume.setIcon(self.volumeMute)

    def muteVolume(self):
        if self.mediaPlayer.isMuted() == True:
            self.mediaPlayer.setMuted(False)
            self.volumeControl(self.volume_2.value())
        else:
            self.mediaPlayer.setMuted(True)
            self.volume.setIcon(self.volumeMute)

    def loopMedia(self):
        if self.repeatMedia == True:
            self.repeatMedia = False
            self.repeat.setIcon(self.repeatDeactive)
        elif self.repeatMedia == False:
            self.repeatMedia = True
            self.repeat.setIcon(self.repeatActive)

    def changetoPlaylist(self):
        from playlist import Ui_playlistWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_playlistWindow(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.playlist = Ui_playlistWindow.playlist

    def playlistPrev(self):
        self.playlist.previous()

    def playlistNext(self):
        self.playlist.next()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 648)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/white Icons/video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#startTime, #endTime{\n"
"    color: #fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame{\n"
"background-color:rgb(0, 13, 20);\n"
"}\n"
"\n"
"QPushButton{\n"
"background: transparent;\n"
"text-align: center;\n"
"font: 75 15pt \"Comic Sans MS\";\n"
"color:  rgb(58, 180, 204);\n"
"border-radius: 30px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.videoWidget = QVideoWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy)
        self.videoWidget.setMinimumSize(QtCore.QSize(700, 200))
##        self.videoWidget.setStyleSheet("background-color: #43549C")
        self.videoWidget.setStyleSheet("background-color: #e33a0b")
        self.videoWidget.setObjectName("videoWidget")
        self.verticalLayout_4.addWidget(self.videoWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startTime = QtWidgets.QLabel(self.frame)
        self.startTime.setObjectName("startTime")
        self.horizontalLayout_2.addWidget(self.startTime)
        self.duration = QtWidgets.QSlider(self.frame)
        self.duration.setMouseTracking(False)
        self.duration.setTabletTracking(False)
        self.duration.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.duration.setAcceptDrops(False)
        self.duration.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.duration.setAutoFillBackground(False)
        self.duration.setStyleSheet("background: transparent;\n"
"-webkit-appearance:round;\n"
"border-radius: 5px;\n"
"color:  rgb(0, 255, 204);\n"
"")
        self.duration.setInputMethodHints(QtCore.Qt.ImhNone)
        self.duration.setSingleStep(1)
        self.duration.setProperty("value", 0)
        self.duration.setSliderPosition(0)
        self.duration.setTracking(True)
        self.duration.setOrientation(QtCore.Qt.Horizontal)
        self.duration.setInvertedAppearance(False)
        self.duration.setInvertedControls(False)
        self.duration.setObjectName("duration")
        self.horizontalLayout_2.addWidget(self.duration)
        self.endTime = QtWidgets.QLabel(self.frame)
        self.endTime.setObjectName("endTime")
        self.horizontalLayout_2.addWidget(self.endTime)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QPushButoon{\n"
"border-radius: 20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.volume = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.volume.setFont(font)
        self.volume.setStyleSheet("#volume:hover{\n"
"icon: url(:/buttons/white Icons/mute-hover.svg);\n"
"cursor: pointer;\n"
"}")
        self.volume.setText("")
        self.volumeMute = QtGui.QIcon()
        self.volumeMute.addPixmap(QtGui.QPixmap(":/buttons/white Icons/mute1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volumeDown = QtGui.QIcon()
        self.volumeDown.addPixmap(QtGui.QPixmap(":/buttons/white Icons/volume-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volumeMed = QtGui.QIcon()
        self.volumeMed.addPixmap(QtGui.QPixmap(":/buttons/white Icons/volume-medium.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volumeUp = QtGui.QIcon()
        self.volumeUp.addPixmap(QtGui.QPixmap(":/buttons/white Icons/volume-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.volume.setIcon(self.volumeUp)
        self.volume.setIconSize(QtCore.QSize(35, 35))
        self.volume.setFlat(False)
        self.volume.setObjectName("volume")
        self.horizontalLayout_6.addWidget(self.volume)
        self.volume_2 = QtWidgets.QSlider(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volume_2.sizePolicy().hasHeightForWidth())
        self.volume_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.volume_2.setFont(font)
        self.volume_2.setMaximum(26)
        self.volume_2.setPageStep(6)
        self.volume_2.setOrientation(QtCore.Qt.Horizontal)
        self.volume_2.setObjectName("volume_2")
        self.horizontalLayout_6.addWidget(self.volume_2)
        self.prev = QtWidgets.QPushButton(self.frame_2)
        self.prev.setStyleSheet("#prev:hover{\n"
"icon: url(:/buttons/cyan icons/previous.svg);\n"
"}")
        self.prev.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/buttons/white Icons/previous (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev.setIcon(icon2)
        self.prev.setIconSize(QtCore.QSize(35, 35))
        self.prev.setObjectName("prev")
        self.horizontalLayout_6.addWidget(self.prev)
        self.play = QtWidgets.QPushButton(self.frame_2)
        self.play.setToolTip("")
        self.play.setStyleSheet("border-radius: 38px;")
        self.play.setText("")
        self.playIcon = QtGui.QIcon()
        self.playIcon.addPixmap(QtGui.QPixmap(":/imgs/cyan icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseIcon = QtGui.QIcon()
        self.pauseIcon.addPixmap(QtGui.QPixmap(":/imgs/cyan icons/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)        
        self.play.setIcon(self.playIcon)
        self.play.setIconSize(QtCore.QSize(70, 70))
        self.play.setObjectName("play")
        self.horizontalLayout_6.addWidget(self.play)
        self.next = QtWidgets.QPushButton(self.frame_2)
        self.next.setStyleSheet("#next:hover{\n"
"icon: url(:/buttons/cyan icons/next (1).svg);\n"
"}")
        self.next.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/buttons/white Icons/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon4)
        self.next.setIconSize(QtCore.QSize(35, 35))
        self.next.setObjectName("next")
        self.horizontalLayout_6.addWidget(self.next)
        self.repeat = QtWidgets.QPushButton(self.frame_2)
        self.repeat.setWhatsThis("")
        self.repeat.setAccessibleName("")
        self.repeat.setAccessibleDescription("")
        self.repeat.setStyleSheet("#repeat{\n"
"border-radius: 10px;\n"
"}\n"
"#repeat:hover{\n"
"icon: url(:/buttons/cyan icons/repeat (1).svg);\n"
"}")
        self.repeat.setText("")
        self.repeatDeactive = QtGui.QIcon()
        self.repeatDeactive.addPixmap(QtGui.QPixmap(":/buttons/white Icons/repeat.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.repeatActive = QtGui.QIcon()
        self.repeatActive.addPixmap(QtGui.QPixmap(":/buttons/cyan icons/repeat (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.repeat.setIcon(self.repeatDeactive)
        self.repeat.setIconSize(QtCore.QSize(35, 35))
        self.repeat.setObjectName("repeat")
        self.horizontalLayout_6.addWidget(self.repeat)
        self.playlistbtn = QtWidgets.QPushButton(self.frame_2)
        self.playlistbtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imgs/cyan icons/playlist.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playlistbtn.setIcon(icon6)
        self.playlistbtn.setIconSize(QtCore.QSize(40, 40))
        self.playlistbtn.setObjectName("playlist")
        self.horizontalLayout_6.addWidget(self.playlistbtn)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1027, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionPlaylist = QtWidgets.QAction(MainWindow)
        self.actionPlaylist.setObjectName("actionPlaylist")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionPlaylist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################### Video Widget ################
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        #################################################

        ################### Video Slider #################
        self.duration.setRange(0,0)
        self.duration.sliderMoved.connect(self.vidPosition)
        self.mediaPlayer.positionChanged.connect(self.locationChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        ##################################################

        ################### Play Button ##################
        self.play.clicked.connect(self.browseFile)
        ##################################################

        ################### Prev Next Buttons ############
        self.prev.pressed.connect(self.playlistPrev)
        self.next.pressed.connect(self.playlistNext)
        ##################################################



        ################### Repeat Button ################
        self.repeat.clicked.connect(self.loopMedia)
        ##################################################

        ################### Volume Icon ##################
        self.volume.clicked.connect(self.muteVolume)
        ##################################################

        ################### Volume Slider ################
        self.volume_2.setRange(0,100)
        self.volume_2.setValue(100)
        self.volume_2.valueChanged.connect(self.volumeControl)
        ##################################################

        ################### Open Button ##################
        self.actionOpen_File.triggered.connect(self.openFile)
        ##################################################

        ################### Close Button #################
        self.actionQuit.triggered.connect(self.closeFile)
        ##################################################

        ################### Playlist Button #################
        self.playlistbtn.clicked.connect(self.changetoPlaylist)
        ##################################################


        self.mediaPlayer.setPlaylist(self.playlist)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player"))
        self.startTime.setText(_translate("MainWindow", "--:--"))
        self.endTime.setText(_translate("MainWindow", "--:--"))
        self.volume.setToolTip(_translate("MainWindow", "volume"))
        self.volume.setShortcut(_translate("MainWindow", "P"))
        self.prev.setToolTip(_translate("MainWindow", "previous"))
        self.prev.setShortcut(_translate("MainWindow", "P"))
        self.play.setShortcut(_translate("MainWindow", "Space"))
        self.next.setToolTip(_translate("MainWindow", "next"))
        self.next.setShortcut(_translate("MainWindow", "N"))
        self.repeat.setToolTip(_translate("MainWindow", "repeat"))
        self.repeat.setShortcut(_translate("MainWindow", "R"))
        self.playlistbtn.setToolTip(_translate("MainWindow", "playlist"))
        self.playlistbtn.setShortcut(_translate("MainWindow", "P"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File..."))
        self.actionPlaylist.setText(_translate("MainWindow", "Playlist"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
import sources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
